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
import requests
import urllib

app = Flask(__name__)
Compress(app)

APPLICATION_NAME = "WebCamOCR"

port = int(os.environ.get('PORT', 5000))

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "secret/service_account.json"

# Show Home page
@app.route('/')
def showHome():
    """Handler for Home page which displays extracted text."""
    return render_template('home.html',
                           title='home')

# Show Source page


@app.route('/source')
def showSource():
    """Handler for Source page which displays extracted text."""
    return render_template('source.html',
                           title='source')

# Show ImageSource-1 page


@app.route('/source/00')
def showImageSource00():
    """Handler for Source page which displays extracted text."""
    return render_template('imagescr00.html',
                           title='image-upload')

# Show ImageSource-2 page


@app.route('/source/01')
def showImageSource01():
    """Handler for Source page which displays extracted text."""
    return render_template('imagescr01.html',
                           title='webcam-capture')

# Show ImageSource-3 page


@app.route('/source/02')
def showImageSource02():
    """Handler for Source page which displays extracted text."""
    return render_template('imagescr02.html',
                           title='image-url')

# Show ImageSource-3 page


@app.route('/t')
def showT():
    """Handler for Source page which displays extracted text."""

    return render_template('translation.html',
                           imageSource='0',
                           title='result')


@app.route('/r')
def showR():
    """Handler for Source page which displays extracted text."""

    return render_template('ocr.html',
                           imageSource='0',
                           title='result')

# Show Result page


@app.route('/image/ocr', methods=['POST'])
def showOCR():
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

        return render_template('ocr.html',
                               ocrResult=ocrResult,
                               imageContainer=request.form['imageContainer'],
                               imageSource=request.form['imageSource'],
                               toLanguage=toLanguage,
                               title='ocr')
    else:
        return render_template('ocr.html',
                               ocrResult='ERROR 400 : Bad Request',
                               title='ocr')

# Show ImageSource-3 page


@app.route('/translate', methods=['GET', 'POST'])
def showTranslate():
    """Handler for Source page which displays extracted text."""
    if request.method == 'POST':
        return render_template('translate.html',
                               translateText=request.form['ocrResult'],
                               title='translate')
    else:
        return render_template('translate.html',
                               title='translate')


# Show Result page
@app.route('/text/translation', methods=['POST'])
def showTranslation():
    """Handler for Result page which displays extracted text."""
    if 'translateText' in request.form and 'toLanguage' in request.form:
        client = translate.Client() 

        if request.form['fromLanguage'] == 'detect':
            response_translate = client.translate(values=request.form['translateText'],
                                        target_language=request.form['toLanguage'])
        else:
            response_translate = client.translate(values=request.form['translateText'],
                                        source_language=request.form['fromLanguage'],
                                        target_language=request.form['toLanguage'])

        if 'translatedText' in response_translate:    
            translationResult = response_translate['translatedText']          
        else:
            translationResult = 'ERROR while fetching translation results.'

        return render_template('translation.html',
                               translateText=request.form['translateText'],
                               translationResult=translationResult,
                               toLanguage=request.form['toLanguage'],
                               title='translation')
    else:
        return render_template('translation.html',
                               translationResult='ERROR 400 : Bad Request',
                               title='translation')


if __name__ == '__main__':
    app.secret_key = get_secret()
    app.debug = True
    app.run(host='0.0.0.0', port=port)
