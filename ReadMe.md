# TextSuite

A web app which uses various APIs to achieve text extraction, text translation and text querying.

## Requirements

To install and run these examples you need:

- [Python 3.7+](https://www.python.org/downloads/ "Python 3.7+")
- [Poetry](https://python-poetry.org/ "Poetry")
- [git](https://git-scm.com/downloads "git") (only to clone this repository)

## Installation

To set up everything in your local machine, you need to follow these steps:

1. Clone this repo and then change directory to the `myapp-textsuite` folder:

```bash
$ git clone https://github.com/kaushalmeena1996/myapp-textsuite.git
$ cd myapp-textsuite
```

2. Install project dependencies using poetry:

```bash
$ poetry install
```

4. Add OCR API Key and Wolfram Alpha Application ID in secrets.json file located in `app/secrets` folder:

- For OCR API Key

  - Sign-up for a Free OCR API Key by visiting this [link](http://eepurl.com/bOLOcf).
  - An API key will be sent to your mail, copy this API key and initialise the 'OCR_API_KEY' variable with your key in secrets.json file.

- For Wolfram Alpha Application ID

  - Sign-up for a Wolfram Alpha Application ID by visiting this [link](https://developer.wolframalpha.com/portal/signup.html). If already signed-up then sign in.
  - After signing in, on the My Apps tab. Click the 'Get an AppID' button and fill out the 'Get a New AppID' form. Use any Application name and description you like.
  - Click the 'Get AppID' button. Copy the APPID string and click 'OK'.
  - Initialise the 'WOLFRAMALPHA_APP_ID' variable with your AppID in secrets.json file.

## Usage

To run the project simply run:

```bash
$ poetry run dev
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deployment

To push to heroku you need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), afterwards you can run these commands:

```bash
$ heroku create
$ git push heroku master
$ heroku open
```

or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
