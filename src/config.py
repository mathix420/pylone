import os
import yaml

from .questions import qload

def get_global_config():
    if not os.path.exists('pylone.yaml'):
        return None
    with open('pylone.yaml') as fp:
        config = yaml.load(fp.read())
    return config


def create_global_config():
    config = qload('global_config')
    save_config(config, '.', 'pylone')
    return config


def save_config(config, path, name='config'):
    with open(os.path.join(path, f'{name}.yaml'), 'w+') as fp:
        yaml.dump(config, fp, default_flow_style=False)


def load_config(path):
    path = os.path.join(path, 'config.yaml')
    if not os.path.exists(path):
        return None
    with open(path) as fp:
        config = yaml.load(fp.read())
    return config
