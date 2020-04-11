import os

from .config import get_global_config, create_global_config
from .utils.changes import detect_changes
from .pylone import PyloneProject
from .questions import ask


def init_app(options):
    config = get_global_config()
    if not config or not ask('A config file was detected would you use it'):
        config = create_global_config()

    project = PyloneProject(options, config)


def create_app(options):
    config = get_global_config()
    if not config:
        exit('No config file found!')
    project = PyloneProject(options, config)
    project.create_archi()

def delete_app(options):
    config = get_global_config()
    if not config:
        exit('No config file found!')
    project = PyloneProject(options, config)
    project.delete_archi()


def push_app(options):
    config = get_global_config()
    if not config:
        exit('No config file found!')
    project = PyloneProject(options, config)
    project.update(options.stage)
    # if not options.functions_only:
    #     project.push_layers()
    # if not options.layers_only:
    #     project.push_functions()
