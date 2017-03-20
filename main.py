# main.py
"""Python script for WebCamOCR implementation."""

# python imports
from flask import Flask, render_template, request, redirect
from flask import url_for
from flask_compress import Compress

from secret.secret import get_secret

from google.cloud import translate, vision

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

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "secret/service_account.json"

# Show Home page
@app.route('/')
def showHome00():
    """Handler for Home page which displays extracted text."""
    return render_template('main-home.html',
                           title='main-home')

# Show Home page
@app.route('/extract')
def showHome01():
    """Handler for Home page which displays extracted text."""
    return render_template('extract-home.html',
                           title='extract-home')

# Show Home page
@app.route('/translate')
def showHome02():
    """Handler for Home page which displays extracted text."""
    return render_template('translate-home.html',
                           title='translate-home')

# Show Home page
@app.route('/query')
def showHome03():
    """Handler for Home page which displays extracted text."""
    return render_template('query-home.html',
                           title='query-home')


# Show Source page


@app.route('/extract/source')
def showSource():
    """Handler for Source page which displays extracted text."""

    browser = request.user_agent.browser
    version = request.user_agent.version and int(request.user_agent.version.split('.')[0])
    platform = request.user_agent.platform
    string = request.user_agent.string
    mobileDevice=0;

    if browser and version:
     if (browser == 'msie' and version < 9) \
      or (browser == 'firefox' and version < 4) \
      or (platform == 'android' and browser == 'safari' and version < 534) \
      or (platform == 'iphone' and browser == 'safari' and version < 7000) \
      or ((platform == 'macos' or platform == 'windows') and browser == 'safari' and not re.search('Mobile', string) and version < 534) \
      or (re.search('iPad', string) and browser == 'safari' and version < 7000) \
      or (platform == 'windows' and re.search('Windows Phone OS', string)) \
      or (browser == 'opera') \
      or (re.search('BlackBerry', string)):
        mobileDevice=1;

    return render_template('extract-source.html',
                            mobileDevice=mobileDevice,
                            title='extract-source')

# Show ImageSource-1 page


@app.route('/extract/source/image-upload')
def showImageSource00():
    """Handler for Source page which displays extracted text."""
    return render_template('extract-source-image-upload.html',
                           title='image-upload')

# Show ImageSource-2 page


@app.route('/extract/source/webcam-capture')
def showImageSource01():
    """Handler for Source page which displays extracted text."""
    return render_template('extract-source-webcam-capture.html',
                           title='webcam-capture')

# Show ImageSource-3 page


@app.route('/extract/source/image-url')
def showImageSource02():
    """Handler for Source page which displays extracted text."""
    return render_template('extract-source-image-url.html',
                           title='image-url')


# Show Result page


@app.route('/extract/result', methods=['POST'])
def showExtractResult():
    """Handler for Result page which displays extracted text."""
    if 'imageUpload' in request.files or 'imageContainer' in request.form:
        client = vision.Client()

        if request.form['imageSource'] == '2':
            image = client.image(content=urllib.urlopen(request.form['imageContainer']).read())
        else:
            image = client.image(content=request.files['imageUpload'].read())

        textList = image.detect_text()
        ocrResult = ''

        if len(textList): 
            ocrResult += textList[0].description  
            toLanguage = textList[0].locale 
        else:
            ocrResult = 'ERROR while fetching ocr results.'
            toLanguage = 'en'

        return render_template('extract-result.html',
                               ocrResult=ocrResult,
                               imageContainer=request.form['imageContainer'],
                               imageSource=request.form['imageSource'],
                               toLanguage=toLanguage,
                               title='extract-result')
    else:
        return render_template('extract-result.html',
                               ocrResult='ERROR 400 : Bad Request',
                               title='extract-result')

# Show ImageSource-3 page


@app.route('/translate/input', methods=['GET', 'POST'])
def showTranslateInput():
    """Handler for Source page which displays extracted text."""
    if request.method == 'POST':
        return render_template('translate-input.html',
                               inputText=request.form['inputText'],
                               title='translate-input')
    else:
        return render_template('translate-input.html',
                               title='translate-input')


# Show Result page
@app.route('/translate/output', methods=['POST'])
def showTranslateOutput():
    """Handler for Result page which displays extracted text."""
    if 'inputText' in request.form and 'toLanguage' in request.form:
        client = translate.Client() 

        if request.form['fromLanguage'] == 'detect':
            response_translate = client.translate(values=request.form['inputText'],
                                        target_language=request.form['toLanguage'])
        else:
            response_translate = client.translate(values=request.form['inputText'],
                                        source_language=request.form['fromLanguage'],
                                        target_language=request.form['toLanguage'])

        if 'translatedText' in response_translate:    
            outputText = response_translate['translatedText']          
        else:
            outputText = 'ERROR while fetching translation results.'

        return render_template('translate-output.html',
                               inputText=request.form['inputText'],
                               outputText=outputText,
                               toLanguage=request.form['toLanguage'],
                               title='translate-output')
    else:
        return render_template('translate-output.html',
                               outputText='ERROR 400 : Bad Request',
                               title='translate-output')



@app.route('/query/input', methods=['GET', 'POST'])
def showQueryInput():
    """Handler for Source page which displays extracted text."""
    if request.method == 'POST':
        return render_template('query-input.html',
                               inputText=request.form['inputText'],
                               title='translate-input')
    else:
        return render_template('query-input.html',
                               title='translate-input')

@app.route('/query/output', methods=['POST'])
def showQueryOutput():
    """Handler for Source page which displays extracted text."""
    if 'inputText' in request.form and 'inputWidth' in request.form:
        appID = json.loads(open('secret/wolframalpha_secret.json', 'r').read())['wolframalpha']['app_id']
        
        queryUrl = 'http://api.wolframalpha.com/v1/simple'
        queryDat = {'appid': appID, 
                    'i': request.form['inputText'],
                    'width': request.form['inputWidth'],
                    'units': 'metric'}

        imageDat = requests.get(queryUrl, queryDat)

        if imageDat.status_code == 200:
            base64Dat = str(base64.b64encode(imageDat.content).decode("utf-8"))
            imageContainer = "data:image/gif;base64," + base64Dat

            return render_template('query-output.html',
                               inputText=request.form['inputText'],
                               imageContainer=imageContainer,
                               title='query-output')
        else:
            queryError = 1
            errorHeader = "ERROR"
            errorContent = imageDat.content

            return render_template('query-output.html',
                                    inputText=request.form['inputText'],
                                    queryError=queryError,
                                    errorHeader=errorHeader,
                                    errorContent=errorContent,
                                    title='query-output')
    else:
        return render_template('query-output.html',
                               queryError=1,
                               errorHeader='ERROR 400',
                               errorContent='input text was not sent correctly',
                               title='query-output')


@app.route('/x')
def x():
    """Handler for Source page which displays extracted text."""
    
    return render_template('extract-result.html',
                           title=text)

@app.route('/t')
def t():
    """Handler for Source page which displays extracted text."""
    return render_template('translate-output.html',
                           title='translate-output')

@app.route('/q')
def q():
    """Handler for Source page which displays extracted text."""
    return render_template('query-output.html',
                           title='query-output')


if __name__ == '__main__':
    app.secret_key = get_secret()
    app.debug = True
    app.run(host='0.0.0.0', port=port)
