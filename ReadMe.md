# [Project : TextSuite]

### [ Synopsis ]
A web app which uses various api to achieve text extraction, text translation and text querying.

#### API USED IN PROJECT:
- text extraction  : OCR API
- text translation : Google Translation API
- text querying    : Wolfram Alpha Simple API

For live version visit page: https://myapp-textsuite.herokuapp.com/

### [Prerequisities]
- Python
  - https://www.python.org/downloads/
- Python Libraries
  - Flask==0.12.2
    - http://flask.pocoo.org/docs/0.11/installation/
  - Flask_Compress==1.4.0
    - https://pypi.python.org/pypi/Flask-Compress
  - user_agents
    - https://pypi.org/project/user-agents/
  - googletrans==2.2.0
    - https://pypi.org/project/googletrans/
  - requests==2.13.0
    - http://docs.python-requests.org/en/master/user/install/

- Free OCR API Key 
  1. Signup for a Free OCR API Key by visiting this [link](http://eepurl.com/bOLOcf).
  2. API key will be sent to your mail, copy this API key and initialise the 'api_key' variable with your key in ocrapi_secret.json file located in secret folder of main directory.

- Wolfram Alpha appID
	 1. Signup for a Wolfram Alpha Application ID by visiting this [link](https://developer.wolframalpha.com/portal/signup.html). If already signedup then signin. 
	 2. After signing in, on the My Apps tab. Click the 'Get an AppID' button and fill out the 'Get a New AppID' form. Use any Application name and description you like.
	 3. Click the 'Get AppID' button. Copy the APPID string and click 'OK'.
	 4. Initialise the 'app_id' variable with your AppID in wolframalpha_secret.json file located in secret folder of main directory.
### [Usage]
To start the app simply run
~~~~
python main.py
~~~~