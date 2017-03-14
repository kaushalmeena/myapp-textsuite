# main.py
"""Python script for WebCamOCR implementation."""

# python imports
from flask import Flask, render_template, request, redirect
from flask import url_for
from flask_compress import Compress


from secret.secret import get_secret

import json
import os
import requests

app = Flask(__name__)
Compress(app)

APPLICATION_NAME = "WebCamOCR"

port = int(os.environ.get('PORT', 5000))


# Show HOME page
@app.route('/', methods=['GET', 'POST'])
def showHome():
    """Handler for Home page which displays welcome message."""
    if request.method == 'POST':
        if 'image_container' in request.form:

            ocrKey = json.loads(open('secret/api_key.json', 'r').read())['ocrapi']['api_key']	
            ocrUrl = "https://api.ocr.space/parse/image"
            ocrDat = { 'apikey': ocrKey, 'base64Image': request.form['image_container'] }

            response = requests.post(url=ocrUrl, data=ocrDat)
            jsonResult = response.json()
            ocrString = ''

            if jsonResult['ErrorMessage'] == None:
                for item in jsonResult['ParsedResults']:
                    ocrString += item['ParsedText']
                ocrResult = ocrString
            else:
                ocrResult = jsonResult['ErrorMessage']
            
            return render_template('home.html',
                                    ocrResult=ocrResult)
        else:
            return render_template('home.html',
                                    ocrResult='Bad Request')
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.secret_key = get_secret()
    app.debug = True
    app.run(host='0.0.0.0', port=port)
