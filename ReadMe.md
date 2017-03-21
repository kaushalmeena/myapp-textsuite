# [Project : TextSuite]

### [ Synopsis ]
A web app which uses various api to achieve text extraction, text translation and text querying.

#### API USED IN PROJECT:
- text extraction  : Google Cloud Vision API (TEXT DETECTION)
- text translation : Google Cloud Translation API
- text querying    : Wolfram Alpha Simple API

For live version visit page: https://myapp-textsuite.herokuapp.com/

### [Prerequisities]
- Google Cloud Service Account 
     1. Open the [Service accounts page](https://console.developers.google.com/permissions/serviceaccounts). If prompted, select a project. If there is no project then create one.
     2. Click Create service account.
     3. In the Create service account window, type a name for the service account, and select Furnish a new private key. If you want to grant G Suite domain-wide authority to the service account, also select Enable G Suite Domain-wide Delegation. 
     4. Click Create. New public/private key pair is generated and downloaded to your machine, save as 'service_account.json' in secret folder of project.
     5. Enable Google Translate API and Google Vision API for your project.
- Wolfram Alpha AppID
	 1. Signup for a Wolfram Alpha Application ID by visiting this [link](https://developer.wolframalpha.com/portal/signup.html). If already signedup then signin. 
	 2. After signing in, on the My Apps tab. Click the 'Get an AppID' button and fill out the 'Get a New AppID' form. Use any Application name and description you like.
	 3. Click the 'Get AppID' button. Copy the APPID string and click "OK".
	 4. Initialise the 'app_id' variable with your AppID in wolframalpha_secret.json file located in secret folder of main directory.
### [Usage]
To start the app simply run
~~~~
python main.py
~~~~