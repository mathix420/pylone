import os
import yaml

from .utils.questions import ask_string, ask_choice


def get_global_config():
	if not os.path.exists('config.yaml'):
		return None
	with open('config.yaml') as fp:
		config = yaml.load(fp.read())
	return config


def create_global_config():
	config = {
		'name': ask_string('Enter a project name'),
		'region': ask_string('Enter the project region'),
		'cloud': ask_choice(
			'Choose a cloud provider',
			['aws', ]
		),
	}
	save_config(config, '.')
	return config


def save_config(config, path):
	with open(os.path.join(path, 'config.yaml'), 'w+') as fp:
		yaml.dump(config, fp, default_flow_style=False)