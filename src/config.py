import yaml
import os
import re

from .questions import qload

variables = re.compile(r'\s(\$[A-Z_]+)\s')


def set_env(fp):
    file = fp.read()
    for var in variables.findall(file):
        file = file.replace(var, os.getenv(var[1:]))
    return file

# TODO: make a custom yaml loader
def get_global_config():
    if not os.path.exists('pylone.yaml'):
        return None
    with open('pylone.yaml') as fp:
        config = yaml.safe_load(set_env(fp))
    return config


def create_global_config():
    config = qload('global_config')
    save_config(config)
    return config


def save_config(config):
    with open('./pylone.yaml', 'w+') as fp:
        yaml.dump(config, fp, default_flow_style=False, indent=2)


def load_config(path):
    path = os.path.join(path, 'config.yaml')
    if not os.path.exists(path):
        return None
    with open(path) as fp:
        config = yaml.load(set_env(fp))
    return config
