import os

def get_env(loader, node):
    value = loader.construct_scalar(node)
    return str(os.getenv(value))
