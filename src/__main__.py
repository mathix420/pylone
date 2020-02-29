from dotenv import load_dotenv
import argparse

from .handlers import (
    init_app,
    push_app,
    create_app,
    delete_app,
)

parser = argparse.ArgumentParser('pylone')
parser.add_argument('--creds-path', '-c', metavar='PATH', type=str, help="Credential path", default=".creds")

# SUBPARSER CONFIG
subparser = parser.add_subparsers(
    dest='action', title='action', description='Pylone actions', required=True)

# INIT
init = subparser.add_parser('init', help='initialize a new project')
init.set_defaults(handler=init_app)

# HOST
host = subparser.add_parser('host', help='host project in the cloud')
host.set_defaults(handler=create_app)

# DELETE
delete = subparser.add_parser('delete', help='delete project from the cloud')
delete.set_defaults(handler=delete_app)

# PUSH
push = subparser.add_parser('push', help='push modifications to the cloud')
push.add_argument('--force-update', '-f', action='store_true', help='force project update', default=False)
push.add_argument('--stage', '-s', type=str, help='project stage', default='dev')
push.add_argument('projects', metavar='NAME', type=str, nargs='*', help='projects to push (all by default)')
push.set_defaults(handler=push_app)


def main():
    load_dotenv('.env')
    options = parser.parse_args()

    if options.handler:
        options.handler(options)
