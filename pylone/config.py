import yaml
import os
import re

from .questions import qload
from .utils.constructors import get_env

variables = re.compile(r'\s(\$[A-Z_]+)\s')
yaml.add_constructor('!env', get_env, yaml.SafeLoader)


def get_global_config():
    if not os.path.exists('pylone.yaml'):
        return None
    with open('pylone.yaml') as fp:
        config = yaml.load(fp, yaml.SafeLoader)
    return config


def create_global_config():
    config = qload('global_config')
    save_config(config)
    return config


def save_config(config):
    with open('./pylone.yaml', 'w+') as fp:
        yaml.dump(config, fp, default_flow_style=False, indent=2)
