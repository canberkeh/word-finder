from pathlib import Path
from flask import Flask
from flasgger import Swagger

app = Flask(__name__)


app.config['SWAGGER'] = {
    'title': 'Word Finder API',
    'uiversion': 3
}

template = {
    "info": {
        "title": "Word Finder API",
        "description": "Word Finder API to find desired word with given length and other options.",
        "contact": {
            "responsibleDeveloper": "canberkeh",
            "email": "canberkehorozal@gmail.com",
            "url": "github.com/canberkeh"
        },
        "version": "1.0.0"
    },
    "consumes": [
        "application/json",
    ],
    "produces": [
        "application/json",
    ],
    "schemes": [
        "http",
        "https"
    ]
}

swagger = Swagger(app, template=template)

from controllers.word_finder import *