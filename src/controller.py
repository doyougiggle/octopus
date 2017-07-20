from sys import argv

import requests
from bottle import route, request, run

models = {
    "en": "english",
    "es": "spanish-ancora",
    "fr": "french",
    "de": "german"
}

url = "https://lindat.mff.cuni.cz/services/udpipe/api/process"


@route('/process', method='POST')
def process():
    success = False
    params = request.params
    if 'text' not in params:
        return {'OK': success}

    text = params["text"]
    if 'lang' in params and models[params["lang"]]:
        lang = params["lang"]
    else:
        lang = models["en"]

    r = requests.post(url, data={'data': text, 'tokenizer': 'normalized_spaces', 'model': lang, 'parser': 'true',
                                 'tagger': 'true'});

    statusCode = r.status_code
    message = r.reason

    if statusCode == 200:
        response = r.json()['result']

    return response


if len(argv) == 3:
    port = argv[2]
    host = argv[1]
elif len(argv) == 2:
    port = argv[1]
    host = '0.0.0.0'
else:
    print("Not enough parameters")
    exit(-1)

run(host=host, port=port, debug=True)
