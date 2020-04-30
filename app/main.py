# main.py
"""Python script for TextSuite server."""

# python imports
from flask import Flask, render_template, request, redirect, url_for
from flask_compress import Compress
from user_agents import parse
from googletrans import Translator
from base64 import b64encode

from app.config import DevelopmentConfig

import requests

app = Flask(__name__)
Compress(app)


@app.route('/')
def home00():
    """Handler for Home00 page which displays main home screen."""
    return render_template('main-home.html',
                           title='main-home')


@app.route('/extract')
def home01():
    """Handler for Home01 page which displays extract home screen."""
    return render_template('extract-home.html',
                           title='extract-home')


@app.route('/translate')
def home02():
    """Handler for Home02 page which displays translate home screen."""
    return render_template('translate-home.html',
                           title='translate-home')


@app.route('/query')
def home03():
    """Handler for Home03 page which displays query home screen."""
    return render_template('query-home.html',
                           title='query-home')


@app.route('/extract/source')
def source():
    """Handler for Source page which displays sources for image upload."""
    user_agent = parse(request.user_agent.string)
    mobile_device = user_agent.is_mobile

    return render_template('extract-source.html',
                           mobile_device=mobile_device,
                           title='extract-source')


@app.route('/extract/source/image-upload')
def image_source00():
    """Handler for Source00 page which provide functionality to upload image via image-upload."""
    return render_template('extract-source-image-upload.html',
                           title='image-upload')


@app.route('/extract/source/webcam-capture')
def image_source01():
    """Handler for Source01 page which provide functionality to upload image via webcam-capture."""
    return render_template('extract-source-webcam-capture.html',
                           title='webcam-capture')


@app.route('/extract/source/image-url')
def image_source02():
    """Handler for Source02 page which provide functionality to upload image via webcam-capture."""
    return render_template('extract-source-image-url.html',
                           title='image-url')


@app.route('/extract/output', methods=['POST'])
def extract_output():
    """Handler for Extract-Output page which displays results for text extraction."""
    template_values = {
        'title': 'extract-output'
    }

    if 'image_container' in request.form and 'image_source' in request.form:
        image_container = request.form.get('image_container')
        image_source = request.form.get('image_source')
        from_language = request.form.get('from_language', 'eng')

        api_key = app.config.get('OCR_API_KEY')
        extract_url = 'https://api.ocr.space/parse/image'

        extract_payload = {
            'apiKey': api_key
        }

        if image_source == 'image-upload' or image_source == 'webcam-capture':
            extract_payload['base64Image'] = image_container
        else:
            extract_payload['url'] = image_container

        if not from_language == 'detect':
            extract_payload['language'] = from_language

        template_values['image_source'] = image_source

        extract_response = requests.post(extract_url, extract_payload)

        if extract_response.status_code == 200:
            json_data = extract_response.json()

            if json_data['OCRExitCode'] == 1:
                output_text = ''

                for response in json_data['ParsedResults']:
                    output_text += response['ParsedText']

                template_values['output_text'] = output_text
            else:
                template_values['error_title'] = 'error'
                template_values['error_content'] = json_data['ErrorMessage'][0]
        else:
            template_values['error_title'] = 'error'
            template_values['error_content'] = extract_response.text
    else:
        template_values['error_title'] = 'error 400'
        template_values['error_content'] = 'bad request'
        template_values['image_source'] = 'image_upload'

    return render_template('extract-output.html', **template_values)


@app.route('/translate/input', methods=['GET', 'POST'])
def translate_input():
    """Handler for Translate-Input page which allow users to enter text to be translated."""
    if request.method == 'POST':
        input_text = request.form.get('input_text')
        return render_template('translate-input.html',
                               input_text=input_text,
                               title='translate-input')
    else:
        return render_template('translate-input.html',
                               title='translate-input')


@app.route('/translate/output', methods=['POST'])
def translate_output():
    """Handler for Translate-Output page which displays results for text translation."""
    template_values = {
        'title': 'translate-output'
    }

    if 'input_text' in request.form and 'to_language' in request.form:
        input_text = request.form.get('input_text')
        to_language = request.form.get('to_language')
        from_language = request.form.get('from_language', 'en')

        translator = Translator()

        if from_language == 'detect':
            translate_response = translator.translate(input_text,
                                                      dest=to_language)
        else:
            translate_response = translator.translate(input_text,
                                                      src=from_language,
                                                      dest=to_language)

        template_values['output_text'] = translate_response.text
    else:
        template_values['error_title'] = 'error 400'
        template_values['error_content'] = 'bad request'

    return render_template('translate-output.html', **template_values)


@app.route('/query/input', methods=['GET', 'POST'])
def query_input():
    """Handler for Query-Input page which allow users to enter text to be queried."""
    if request.method == 'POST':
        input_text = request.form.get('input_text')
        return render_template('query-input.html',
                               input_text=input_text,
                               title='query-input')
    else:
        return render_template('query-input.html',
                               title='query-input')


@app.route('/query/output', methods=['POST'])
def query_output():
    """Handler for Query-Output page which displays results for text querying."""
    template_values = {
        'title': 'translate-output'
    }

    if 'input_text' in request.form:
        input_text = request.form.get('input_text')

        app_id = app.config.get("WOLFRAMALPHA_APP_ID")
        query_url = 'http://api.wolframalpha.com/v1/simple'

        query_payload = {
            'appid': app_id,
            'i': input_text,
            'width': 500,
            'units': 'metric'
        }

        query_response = requests.get(query_url, query_payload)

        if query_response.status_code == 200:
            query_content = query_response.content
            base_64_data = str(b64encode(query_content).decode('utf-8'))

            image_container = 'data:image/gif;base64,' + base_64_data

            template_values['image_container'] = image_container
        else:
            template_values['error_title'] = 'error'
            template_values['error_content'] = 'internal server error'
    else:
        template_values['error_title'] = 'error 400'
        template_values['error_content'] = 'bad request'

    return render_template('query-output.html', **template_values)


def start():
    """Start flask development server"""
    app.config.from_object(DevelopmentConfig())
    app.run()


if __name__ == "__main__":
    app.config.from_object(DevelopmentConfig())
    app.run()
