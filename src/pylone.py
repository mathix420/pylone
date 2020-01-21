from .config import save_config, load_config
from .providers import providers
from .utils.dirs import makedirs
from .questions import qload


class PyloneProject():
    functions = dict()
    layers = dict()

    def __init__(self, options, config):
        self.config = config
        self.options = options
        self.provider = providers[config['cloud']](config)
        # init functions
        for fct in self.config.get('functions', []):
            if not fct in self.functions:
                self.functions[fct] = load_config(fct)
        # init layers
        for layer in self.config.get('layers', []):
            if not layer in self.layers:
                self.layers[layer] = load_config(layer)

    def _save_state(self):
        self.config['functions'] = list(self.functions.keys())
        self.config['layers'] = list(self.layers.keys())
        print('SAVE STATE')
        print(self.functions)
        print(self.layers)
        print(self.config)
        save_config(self.config, '.', 'pylone')

    def create_function(self):
        config = qload('create_function')
        makedirs([config['name']])
        save_config(config, config['name'])
        self.functions[config['name']] = config
        self._save_state()

    def create_layer(self):
        config = qload('create_layer')
        makedirs([config['name']])
        save_config(config, config['name'])
        self.layers[config['name']] = config
        self._save_state()

    def push_functions(self):
        print('push functions')
        print(self.functions)
        for name, config in self.functions:
            self.provider.push_function(name, config)

    def push_layers(self):
        print('push layers')
        print(self.layers)
