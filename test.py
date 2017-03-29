import json
import os
import re
import requests
import urllib
import base64

text =  {
 "data": {
  "translations": [
   {
    "translatedText": "adsfaf",
    "detectedSourceLanguage": "en"
   }
  ]
 }
}
 
print text['data']['translations'][0]['translatedText']

