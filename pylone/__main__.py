from dotenv import load_dotenv
from os import getenv
import argparse

from .utils.doppler import load_doppler
from .handlers import (
    init_app,
    push_app,
    create_app,
    delete_app,
)

parser = argparse.ArgumentParser('pylone')
parser.add_argument('--creds-path', '-c', metavar='PATH', type=str, help="Credential path", default=".creds")
parser.add_argument('--doppler-project', '--dp', metavar='PROJECT', type=str, help="Doppler project id")
parser.add_argument('--doppler-config', '--dc', metavar='CONFIG', type=str, help="Doppler config name")
parser.add_argument('--doppler-token', '--dt', metavar='TOKEN', type=str, help="Doppler service token", default=getenv('DOPPLER_TOKEN'))

# SUBPARSER CONFIG
subparser = parser.add_subparsers(
    dest='action', title='action', description='Pylone actions', required=True)

# INIT
init = subparser.add_parser('init', help='initialize a new project')
init.add_argument('--objects', '-o', metavar='NAME', type=str, nargs='*', help='objects to push (all by default)')
init.set_defaults(handler=init_app)

# HOST
host = subparser.add_parser('host', help='host project in the cloud')
host.add_argument('--objects', '-o', metavar='NAME', type=str, nargs='*', help='objects to push (all by default)')
host.set_defaults(handler=create_app)

# DELETE
delete = subparser.add_parser('delete', help='delete project from the cloud')
delete.add_argument('--objects', '-o', metavar='NAME', type=str, nargs='*', help='objects to push (all by default)')
delete.set_defaults(handler=delete_app)

# PUSH
push = subparser.add_parser('push', help='push modifications to the cloud')
push.add_argument('--objects', '-o', metavar='NAME', type=str, nargs='*', help='objects to push (all by default)')
push.add_argument('--force-update', '-f', action='store_true', help='force project update', default=False)
push.add_argument('--stage', '-s', type=str, help='project stage', default='dev')
push.set_defaults(handler=push_app)


def main():
    options = parser.parse_args()
    if options.doppler_token:
        load_doppler(options)
    else:
        load_dotenv('.env')

    if options.handler:
        options.handler(options)
