# [Project : OCR Website]

### [ Synopsis ]
A web app which uses Google Vision API to convert image to text via various sources.

- For live version visit page: https://myapp-image2text.herokuapp.com/

### [Prerequisities]
- Google Cloud Service Account 
     1. Open the [Service accounts page](https://console.developers.google.com/permissions/serviceaccounts). If prompted, select a project. If there is no project then create one.
     2. Click Create service account.
     3. In the Create service account window, type a name for the service account, and select Furnish a new private key. If you want to grant G Suite domain-wide authority to the service account, also select Enable G Suite Domain-wide Delegation. 
     4.Click Create. New public/private key pair is generated and downloaded to your machine, save as 'service_account.json' in secret folder of project.
     5.Enable Google Translate API and Google Vision API for your project.
### [Usage]
To start the app simply run
~~~~
python main.py
~~~~