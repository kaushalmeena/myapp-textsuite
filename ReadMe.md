# [Project : TextSuite]

### [ Synopsis ]
A web app which uses various api to achieve text extraction, text translation and text querying.

#### API USED IN PROJECT:
- text extraction  : Google Cloud Vision API (TEXT DETECTION)
- text translation : Google Cloud Translation API
- text querying    : Wolfram Alpha Simple API

For live version visit page: https://myapp-textsuite.herokuapp.com/

### [Prerequisities]
- Google Cloud apiKey 
     1. Go to the [Google API Console Credentials](https://console.cloud.google.com/apis/credentials). If prompted, select a project. If there is no project then create one.
     2. Click Create credentials, select API key
     3. Copy API key from dialog box and initialise the 'api_key' variable with your apiKey in googlecloud_secret.json file located in secret folder of main directory.
     5. Enable Google Translate API and Google Vision API for your project.
- Wolfram Alpha appID
	 1. Signup for a Wolfram Alpha Application ID by visiting this [link](https://developer.wolframalpha.com/portal/signup.html). If already signedup then signin. 
	 2. After signing in, on the My Apps tab. Click the 'Get an AppID' button and fill out the 'Get a New AppID' form. Use any Application name and description you like.
	 3. Click the 'Get AppID' button. Copy the APPID string and click "OK".
	 4. Initialise the 'app_id' variable with your AppID in wolframalpha_secret.json file located in secret folder of main directory.
### [Usage]
To start the app simply run
~~~~
python main.py
~~~~