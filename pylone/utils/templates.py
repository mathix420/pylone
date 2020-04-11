import yaml


def fct_template(config, dest):
	"""
	This function build the function config file.
	"""
	with open(dest, 'w+') as fp:
		yaml.dump({
			'name': config['name'],
			'timeout': config['timeout'],
			'handler': config['handler'],
			'runtime': config['runtime'],
			'role': config['role']
		}, fp)
