# TextSuite

A web app which uses various APIs to achieve text extraction, text translation and text querying.

## Requirements

To install and run this project you need:

- [Python 3.7+](https://www.python.org/downloads/ "Python 3.7+")
- [Poetry](https://python-poetry.org/ "Poetry")
- [git](https://git-scm.com/downloads "git") (only to clone this repository)

## Installation

To set up everything in your local machine, you need to follow these steps:

1. Clone this repo and then change directory to the `myapp-textsuite` folder:

```bash
$ git clone https://github.com/kaushalmeena/myapp-textsuite.git
$ cd myapp-textsuite
```

2. Install project dependencies using poetry:

```bash
$ poetry install
```

3. Create `.env` file by creating copy of `.env.default` file:

```bash
$ cp .env.default .env
```

4. Add OCR API Key and Wolfram Alpha Application ID in `.env` file:

- For OCR API Key

  - Sign-up for a Free OCR API Key by visiting this [link](http://eepurl.com/bOLOcf).
  - An API key will be sent to your mail, copy this API key and initialise the 'OCR_API_KEY' variable with your key in `.env` file.

- For Wolfram Alpha Application ID

  - Sign-up for a Wolfram Alpha Application ID by visiting this [link](https://developer.wolframalpha.com/portal/signup.html). If already signed-up then sign in.
  - After signing in, on the My Apps tab. Click the 'Get an AppID' button and fill out the 'Get a New AppID' form. Use any Application name and description you like.
  - Click the 'Get AppID' button. Copy the APPID string and click 'OK'.
  - Initialise the 'WOLFRAMALPHA_APP_ID' variable with your AppID in `.env` file.

## Usage

To run the project simply run:

```bash
$ poetry run python wsgi.py
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deployment

To push to Heroku you need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) afterwards, you can run these commands:

```bash
$ heroku create
$ heroku config:set OCR_API_KEY='<YOUR-API-KEY-HERE>'
$ heroku config:set WOLFRAMALPHA_APP_ID='<YOUR-APP-ID-HERE>'
$ git push heroku master
$ heroku open
```

or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
