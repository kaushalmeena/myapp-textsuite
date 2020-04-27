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

3. Change directory to the `app` folder and create `.env` file from `.env.default`:

```bash
$ cd app
$ cp .env.default .env
```

4. Add OCR API Key in .env file:

   1. Signup for a Free OCR API Key by visiting this [link](http://eepurl.com/bOLOcf).
   2. An API key will be sent to your mail, copy this API key and initialise the 'OCR_API_KEY' variable with your key in .env file.

5. Add Wolfram Alpha Application ID in .env file:

   1. Signup for a Wolfram Alpha Application ID by visiting this [link](https://developer.wolframalpha.com/portal/signup.html). If already signed-up then sign in.
   2. After signing in, on the My Apps tab. Click the 'Get an AppID' button and fill out the 'Get a New AppID' form. Use any Application name and description you like.
   3. Click the 'Get AppID' button. Copy the APPID string and click 'OK'.
   4. Initialise the 'WOLFRAMALPHA_APP_ID' variable with your AppID in .env file.

## Usage

To start the project simply run:

```bash
$ poetry run dev
```
