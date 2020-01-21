import argparse

from .handlers import (
    init_app,
    push_app,
    create_fct,
    create_layer,
)


parser = argparse.ArgumentParser('pylone')
subparser = parser.add_subparsers(
    dest='action',
    title='action',
    description='Pylone actions',
    required=True
)

init = subparser.add_parser(
    'init',
    help='initialise a new project',
)
init.set_defaults(handler=init_app)

_create_fct = subparser.add_parser(
    'create-function',
    help='create a new function',
)
_create_fct.set_defaults(handler=create_fct)

_create_layer = subparser.add_parser(
    'create-layer',
    help='create a new layer',
)
_create_layer.set_defaults(handler=create_layer)

push = subparser.add_parser(
    'push',
    help='create a new layer',
)
push.add_argument(
    '--functions-only', '-f',
    action='store_true',
    help='push only functions'
)
push.add_argument(
    '--layers-only', '-l',
    action='store_true',
    help='push only layers'
)
push.set_defaults(handler=push_app)


def main():
    options = parser.parse_args()

    if options.handler:
        options.handler(options)
