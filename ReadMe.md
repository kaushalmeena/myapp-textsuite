# [Project : TextSuite]

### [ Synopsis ]
A web app which uses various api to achieve text extraction, text translation and text querying.

#### API USED IN PROJECT:
- text extraction  : Google Cloud Vision API (TEXT DETECTION)
- text translation : Google Cloud Translation API
- text querying    : Wolfram Alpha Simple API

For live version visit page: https://myapp-textsuite.herokuapp.com/

### [Prerequisities]
- Python
  - https://www.python.org/downloads/
- Python Libraries
  - Flask==0.9
    - http://flask.pocoo.org/docs/0.11/installation/
  - oauth2client==3.0.0
    - https://oauth2client.readthedocs.io/en/latest/
  - httplib2==0.9.2
    - https://pypi.python.org/pypi/httplib2
  - SQLAlchemy==1.0.15
    - http://www.sqlalchemy.org/download.html
  - requests==2.11.1
    - http://docs.python-requests.org/en/master/user/install/

- Google Cloud apiKey 
     1. Go to the [Google API Console Credentials](https://console.cloud.google.com/apis/credentials). If prompted, select a project. If there is no project then create one.
     2. Click Create credentials, select API key
     3. Copy API key from dialog box and initialise the 'api_key' variable with your apiKey in googlecloud_secret.json file located in secret folder of main directory.
     4. In the dialog box click on restrict key, then in Key restriction select 'HTTP referrers (websites)'. Enter 'https://myapp-textsuite.herokuapp.com/' in textbox, then click save.
     5. Enable [Google Translate API](https://console.cloud.google.com/apis/api/translate.googleapis.com/) and [Google Vision API](https://console.cloud.google.com/apis/api/vision.googleapis.com/) for your project.
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