from dotenv import load_dotenv
import argparse

from .handlers import (
    init_app,
    push_app,
    create_app,
    delete_app,
)

parser = argparse.ArgumentParser('pylone')

parser.add_argument('--creds-path', '-c', type=str,
                    help="Credential path", default=".creds")

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

init = subparser.add_parser(
    'host',
    help='host the project in cloud',
)
init.set_defaults(handler=create_app)

init = subparser.add_parser(
    'delete',
    help='delete the project from the cloud',
)
init.set_defaults(handler=delete_app)

push = subparser.add_parser(
    'push',
    help='push modifications to the cloud',
)
push.add_argument(
    '--force-update', '-f', action='store_true', help='project stage', default=False
)
push.add_argument(
    '--stage', '-s', type=str, help='project stage', required=True
)
push.set_defaults(handler=push_app)


def main():
    load_dotenv('.env')
    options = parser.parse_args()

    if options.handler:
        options.handler(options)
