import argparse

from .handlers import (
	init_app,
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

create_fct = subparser.add_parser(
	'create-function',
	help='create a new function',
)
create_fct.set_defaults(handler=create_fct)

create_layer = subparser.add_parser(
	'create-layer',
	help='create a new layer',
)
create_layer.set_defaults(handler=create_layer)


def main():
	options = parser.parse_args()

	if options.handler:
		options.handler(options)
