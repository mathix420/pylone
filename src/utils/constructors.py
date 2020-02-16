import os

def get_env(loader, node):
    value = loader.construct_scalar(node)
    print(value)
    return os.getenv(value)