# main.py
"""Python script for TextSuite server."""

# python imports
from flask import Flask, render_template, request, redirect
from flask import url_for
from flask_compress import Compress

from user_agents import parse

from googletrans import Translator

from app.config import DevelopmentConfig

import json
import os
import re
import requests
import urllib
import base64

app = Flask(__name__)
Compress(app)

# Main Home page
@app.route('/')
def home00():
    """Handler for Home00 page which displays main home screen."""
    return render_template('main-home.html',
                           title='main-home')

# Extract Home page
@app.route('/extract')
def home01():
    """Handler for Home01 page which displays extract home screen."""
    return render_template('extract-home.html',
                           title='extract-home')

# Translate Home page
@app.route('/translate')
def home02():
    """Handler for Home02 page which displays translate home screen."""
    return render_template('translate-home.html',
                           title='translate-home')

# Query Home page
@app.route('/query')
def home03():
    """Handler for Home03 page which displays query home screen."""
    return render_template('query-home.html',
                           title='query-home')


# Source page
@app.route('/extract/source')
def source():
    """Handler for Source page which displays sources for image upload."""
    user_agent = parse(request.user_agent.string)
    mobile_device = user_agent.is_mobile

    return render_template('extract-source.html',
                           mobile_device=mobile_device,
                           title='extract-source')

# Image Source (image-upload) page
@app.route('/extract/source/image-upload')
def image_source00():
    """Handler for Source00 page which provide functionality to upload image via image-upload."""
    return render_template('extract-source-image-upload.html',
                           title='image-upload')

# Image Source (webcam-capture) page
@app.route('/extract/source/webcam-capture')
def image_source01():
    """Handler for Source01 page which provide functionality to upload image via webcam-capture."""
    return render_template('extract-source-webcam-capture.html',
                           title='webcam-capture')

# Image Source (image-url) page
@app.route('/extract/source/image-url')
def image_source02():
    """Handler for Source02 page which provide functionality to upload image via webcam-capture."""
    return render_template('extract-source-image-url.html',
                           title='image-url')


# Extract Result page
@app.route('/extract/result', methods=['POST'])
def extract_result():
    """Handler for Extract-Result page which displays results for text extraction."""
    if 'image_container' in request.form:
        api_key = app.config.get("OCR_API_KEY")
        extract_url = "https://api.ocr.space/parse/image"

        if request.form['image_source'] == '0' or request.form['image_source'] == '1':
            image_content = request.form['image_container']
        else:
            image_content = base64.b64encode(
                urllib.request.urlopen(request.form['image_container']).read())

        if request.form['from_language'] == 'detect':
            from_language = 'en'
            extract_payload = {
                "apiKey": api_key,
                "base64Image": image_content
            }

        else:
            from_language = request.form['from_language']
            extract_payload = {
                "apiKey": api_key,
                "base64Image": image_content,
                "language": request.form['from_language']
            }

        extract_response = requests.post(extract_url, extract_payload)

        if extract_response.status_code == 200:
            extract_response = extract_response.json()
            ocr_result = ''
            for response in extract_response['ParsedResults']:
                ocr_result += response['ParsedText']

        else:
            extract_response = extract_response.json()
            ocr_result = extract_response['ErrorDetails']

        return render_template('extract-result.html',
                               ocr_result=ocr_result,
                               image_container=request.form['image_container'],
                               image_source=request.form['image_source'],
                               from_language=from_language,
                               title='extract-result')
    else:
        return render_template('extract-result.html',
                               ocr_result='ERROR 400 : Bad Request',
                               title='extract-result')

# Translate Input page
@app.route('/translate/input', methods=['GET', 'POST'])
def translate_input():
    """Handler for Translate-Input page which allow users to enter text to be translated."""
    if request.method == 'POST':
        return render_template('translate-input.html',
                               input_text=request.form['input_text'],
                               title='translate-input')
    else:
        return render_template('translate-input.html',
                               title='translate-input')

# Translate Output page
@app.route('/translate/output', methods=['POST'])
def translate_output():
    """Handler for Translate-Output page which displays results for text translation."""
    if 'input_text' in request.form and 'to_language' in request.form:
        translator = Translator()

        if request.form['from_language'] == 'detect':
            translate_response = translator.translate(request.form['input_text'],
                                                      dest=request.form['to_language'])
        else:
            translate_response = translator.translate(request.form['input_text'],
                                                      src=request.form['from_language'],
                                                      dest=request.form['to_language'])

        output_text = translate_response.text

        return render_template('translate-output.html',
                               input_text=request.form['input_text'],
                               output_text=output_text,
                               to_language=request.form['to_language'],
                               title='translate-output')
    else:
        return render_template('translate-output.html',
                               output_text='ERROR 400 : Bad Request',
                               title='translate-output')

# Query Input page
@app.route('/query/input', methods=['GET', 'POST'])
def query_input():
    """Handler for Query-Input page which allow users to enter text to be queried."""
    if request.method == 'POST':
        return render_template('query-input.html',
                               input_text=request.form['input_text'],
                               title='translate-input')
    else:
        return render_template('query-input.html',
                               title='translate-input')

# Query Output page
@app.route('/query/output', methods=['POST'])
def query_output():
    """Handler for Query-Output page which displays results for text querying."""
    user_agent = parse(request.user_agent.string)
    mobile_device = user_agent.is_mobile

    if 'input_text' in request.form and 'input_width' in request.form:
        app_id = app.config.get("WOLFRAMALPHA_APP_ID")
        query_url = 'http://api.wolframalpha.com/v1/simple'
        query_payload = {'appid': app_id,
                         'i': request.form['input_text'],
                         'width': request.form['input_width'],
                         'units': 'metric'}

        query_response = requests.get(query_url, query_payload)

        if query_response.status_code == 200:
            base_64_data = str(base64.b64encode(
                query_response.content).decode("utf-8"))
            image_container = "data:image/gif;base64," + base_64_data

            return render_template('query-output.html',
                                   input_text=request.form['input_text'],
                                   image_container=image_container,
                                   mobile_device=mobile_device,
                                   title='query-output')
        else:
            error_header = "ERROR"
            error_content = query_response.text

            return render_template('query-output.html',
                                   input_text=request.form['input_text'],
                                   query_error=True,
                                   error_header=error_header,
                                   error_content=error_content,
                                   mobile_device=mobile_device,
                                   title='query-output')
    else:
        return render_template('query-output.html',
                               query_error=True,
                               error_header='ERROR 400',
                               error_content='input text was not sent correctly',
                               mobile_device=mobile_device,
                               title='query-output')


def start():
    """Start flask development server"""
    app.config.from_object(DevelopmentConfig())
    app.run()


if __name__ == "__main__":
    start()
