import os
import json
from PyInquirer import prompt
from . import (
    create_function,
    global_config,
    create_layer,
    credentials,
)

QUESTIONS = {
    'create_function': create_function.questions,
    'create_layer': create_layer.questions,
    'credentials': credentials.questions,
    'global_config': global_config.questions,
}


def ask(message, default=True):
    question = [
        {
            'type': 'confirm',
            'name': 'out',
            'message': message,
            'default': default
        }
    ]
    return prompt(question).get('out', default)


def qload(fct_name):
    '''
    Load and ask a question file.
    '''
    return prompt(QUESTIONS[fct_name])
