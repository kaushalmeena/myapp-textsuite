# main.py
"""Python script for TextSuite implementation."""

# python imports
from flask import Flask, render_template, request, redirect
from flask import url_for
from flask_compress import Compress

from secret.secret import get_secret

from user_agents import parse

import json
import os
import re
import requests
import urllib
import base64


app = Flask(__name__)
Compress(app)

APPLICATION_NAME = "TextSuite"

port = int(os.environ.get('PORT', 5000))

# Show Main Home page


@app.route('/')
def showHome00():
    """Handler for Home00 page which displays main home screen."""
    return render_template('main-home.html',
                           title='main-home')

# Show Extract Home page


@app.route('/extract')
def showHome01():
    """Handler for Home01 page which displays extract home screen."""
    return render_template('extract-home.html',
                           title='extract-home')

# Show Translate Home page


@app.route('/translate')
def showHome02():
    """Handler for Home02 page which displays translate home screen."""
    return render_template('translate-home.html',
                           title='translate-home')

# Show Query Home page


@app.route('/query')
def showHome03():
    """Handler for Home03 page which displays query home screen."""
    return render_template('query-home.html',
                           title='query-home')


# Show Source page


@app.route('/extract/source')
def showSource():
    """Handler for Source page which displays sources for image upload."""
    user_agent = parse(request.user_agent.string)
    mobileDevice = user_agent.is_mobile

    return render_template('extract-source.html',
                           mobileDevice=mobileDevice,
                           title='extract-source')

# Show Image Source (image-upload) page


@app.route('/extract/source/image-upload')
def showImageSource00():
    """Handler for Source00 page which provide functionality to upload image via image-upload."""
    return render_template('extract-source-image-upload.html',
                           title='image-upload')

# Show Image Source (webcam-capture) page


@app.route('/extract/source/webcam-capture')
def showImageSource01():
    """Handler for Source00 page which provide functionality to upload image via webcam-capture."""
    return render_template('extract-source-webcam-capture.html',
                           title='webcam-capture')

# Show Image Source (image-url) page


@app.route('/extract/source/image-url')
def showImageSource02():
    """Handler for Source00 page which provide functionality to upload image via webcam-capture."""
    return render_template('extract-source-image-url.html',
                           title='image-url')


# Show Extract Result page


@app.route('/extract/result', methods=['POST'])
def showExtractResult():
    """Handler for ExtractResult page which displays results for text extraction."""
    if 'imageContainer' in request.form:
        apiKey = json.loads(
            open('secret/googlecloud_secret.json', 'r').read())['googlecloud']['api_key']

        extractUrl = "https://vision.googleapis.com/v1/images:annotate"

        if request.form['imageSource'] == '0' or request.form['imageSource'] == '1':
            imageContent = request.form['imageContainer'].split(',')[1]
        else:
            imageContent = base64.b64encode(urllib.urlopen(
                request.form['imageContainer']).read())

        if request.form['fromLanguage'] == 'detect':
            extractDat = {
                "requests": [
                    {
                        "image": {
                            "content": imageContent
                        },
                        "features": [
                            {
                                "type": "TEXT_DETECTION",
                                "maxResults": 1
                            }
                        ]
                    }
                ]
            }
        else:
            extractDat = {
                "requests": [
                    {
                        "image": {
                            "content": imageContent
                        },
                        "features": [
                            {
                                "type": "TEXT_DETECTION",
                                "maxResults": 1
                            }
                        ],
                        "imageContext": {
                            "languageHints": request.form['fromLanguage']
                        },
                    }
                ]
            }

        extractResponse = requests.post("%s?key=%s" % (extractUrl, apiKey), json.dumps(
            extractDat), headers={'content-type': 'application/json', 'Referer': 'https://myapp-textsuite.herokuapp.com/'})

        if extractResponse.status_code != 200 or extractResponse.json().get('error'):
            ocrResult = extractResponse.text
            fromLanguage = 'en'

        else:
            extractResponse = extractResponse.json()
            ocrResult = extractResponse['responses'][
                0]['textAnnotations'][0]['description']

            if request.form['fromLanguage'] == 'detect':
                fromLanguage = extractResponse['responses'][0][
                    'textAnnotations'][0]['locale'].split('-')[0]
            else:
                fromLanguage = request.form['fromLanguage']

        return render_template('extract-result.html',
                               ocrResult=ocrResult,
                               imageContainer=request.form['imageContainer'],
                               imageSource=request.form['imageSource'],
                               fromLanguage=fromLanguage,
                               title='extract-result')
    else:
        return render_template('extract-result.html',
                               ocrResult='ERROR 400 : Bad Request',
                               title='extract-result')

# Show Translate Input page


@app.route('/translate/input', methods=['GET', 'POST'])
def showTranslateInput():
    """Handler for TranslateInput page which allow users to enter text to be translated."""
    if request.method == 'POST':
        return render_template('translate-input.html',
                               inputText=request.form['inputText'],
                               title='translate-input')
    else:
        return render_template('translate-input.html',
                               title='translate-input')

# Show Translate Output page


@app.route('/translate/output', methods=['POST'])
def showTranslateOutput():
    """Handler for TranslateOutput page which displays results for text translation."""
    if 'inputText' in request.form and 'toLanguage' in request.form:
        apiKey = json.loads(
            open('secret/googlecloud_secret.json', 'r').read())['googlecloud']['api_key']

        translateUrl = "https://www.googleapis.com/language/translate/v2"

        if request.form['fromLanguage'] == 'detect':
            translateDat = {'key': apiKey,
                            'q': request.form['inputText'],
                            'format': 'text',
                            'target': request.form['toLanguage']}
        else:
            translateDat = {'key': apiKey,
                            'q': request.form['inputText'],
                            'format': 'text',
                            'target': request.form['toLanguage'],
                            'source': request.form['fromLanguage']}

        translateResponse = requests.get(translateUrl, translateDat, headers={
                                         'Referer': 'https://myapp-textsuite.herokuapp.com/'})

        if translateResponse.status_code != 200 or translateResponse.json().get('error'):
            outputText = translateResponse.text

        else:
            translateResponse = translateResponse.json()
            outputText = translateResponse['data'][
                'translations'][0]['translatedText']

        return render_template('translate-output.html',
                               inputText=request.form['inputText'],
                               outputText=outputText,
                               toLanguage=request.form['toLanguage'],
                               title='translate-output')
    else:
        return render_template('translate-output.html',
                               outputText='ERROR 400 : Bad Request',
                               title='translate-output')

# Show Query Input page


@app.route('/query/input', methods=['GET', 'POST'])
def showQueryInput():
    """Handler for QueryInput page which allow users to enter text to be queried."""
    if request.method == 'POST':
        return render_template('query-input.html',
                               inputText=request.form['inputText'],
                               title='translate-input')
    else:
        return render_template('query-input.html',
                               title='translate-input')

# Show Query Output page


@app.route('/query/output', methods=['POST'])
def showQueryOutput():
    """Handler for QueryOutput page which displays results for text querying."""
    user_agent = parse(request.user_agent.string)
    mobileDevice = user_agent.is_mobile

    if 'inputText' in request.form and 'inputWidth' in request.form:
        appID = json.loads(
            open('secret/wolframalpha_secret.json', 'r').read())['wolframalpha']['app_id']

        queryUrl = 'http://api.wolframalpha.com/v1/simple'
        queryDat = {'appid': appID,
                    'i': request.form['inputText'],
                    'width': request.form['inputWidth'],
                    'units': 'metric'}

        queryResponse = requests.get(queryUrl, queryDat)

        if queryResponse.status_code == 200:
            base64Dat = str(base64.b64encode(
                queryResponse.content).decode("utf-8"))
            imageContainer = "data:image/gif;base64," + base64Dat

            return render_template('query-output.html',
                                   inputText=request.form['inputText'],
                                   imageContainer=imageContainer,
                                   mobileDevice=mobileDevice,
                                   title='query-output')
        else:
            errorHeader = "ERROR"
            errorContent = queryResponse.text

            return render_template('query-output.html',
                                   inputText=request.form['inputText'],
                                   queryError=True,
                                   errorHeader=errorHeader,
                                   errorContent=errorContent,
                                   mobileDevice=mobileDevice,
                                   title='query-output')
    else:
        return render_template('query-output.html',
                               queryError=True,
                               errorHeader='ERROR 400',
                               errorContent='input text was not sent correctly',
                               mobileDevice=mobileDevice,
                               title='query-output')

if __name__ == '__main__':
    app.secret_key = get_secret()
    app.debug = True
    app.run(host='0.0.0.0', port=port)
