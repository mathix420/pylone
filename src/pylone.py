from .utils.questions import (
	ask_list,
	ask_string,
	ask_list_choices,
)
from .utils.dirs import makedirs
from .config import save_config


class PyloneProject():
	functions = dict()
	layers = dict()

	def __init__(self, options, config):
		self.options = options
		self.config = config
		pass

	def create_function(self):
		config = {
			'name': ask_string('Enter function name'),
			'description': ask_string('Enter a description for the function'),
			'runtime': ask_string('Enter the function runtime'),
			'layers': ask_list_choices(
				'Choose layers', self.layers.keys(), True
			),
			'timeout': int(ask_string('Enter the function timeout (in sec)')),
			'handler': ask_string('Enter the function handler (file.fct)'),
			'role': ask_string('Enter the function role'),
		}
		makedirs([config['name']])
		save_config(config, config['name'])
		self.functions[config['name']] = config


	def create_layer(self):
		config = {
			'name': ask_string('Enter layer name'),
			'description': ask_string('Enter a description for the layer'),
			'runtime': ask_list('Enter a runtime'),
		}
		makedirs([config['name']])
		save_config(config, config['name'])
		self.layers[config['name']] = config
