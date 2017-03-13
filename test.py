import json


t = {u'ErrorDetails': None, u'ErrorMessage': None, u'OCRExitCode': 1, u'ParsedResults': [{u'ParsedText': u'O Note \r\nThe basic installation works on Windows and OS X using the binaries from PyPl. Other \r\ninstallations require building from source as detailed below. \r\n', u'FileParseExitCode': 1, u'ErrorMessage': u'', u'TextOverlay': {u'HasOverlay': False, u'Lines': [], u'Message': u'Text overlay is not provided as it is not requested'}, u'ErrorDetails': u''}], u'IsErroredOnProcessing': False, u'ProcessingTimeInMilliseconds': u'2544'}

for item in t['ParsedResults']:
	result +=  item['ParsedText']
print result