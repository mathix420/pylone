from .config import save_config
from .providers import providers
from .utils.dirs import makedirs
from .utils.scripts import run
from .questions import qload

from .functions import PyloneFct
from .layers import PyloneLayer
from .apis import PyloneApi


class PyloneProject():
    functions = list()
    layers = list()
    apis = list()

    def __init__(self, options, config):
        self.config = config
        self.options = options
        self.provider = providers[config['cloud']](config, options)
        self._init_classes()

    def _init_classes(self):
        gcf = {
            'provider': self.provider,
        }
        for cfg in self.config.get('functions', {}).values():
            self.functions.append(PyloneFct(cfg, gcf))
        for cfg in self.config.get('layers', {}).values():
            self.layers.append(PyloneLayer(cfg, gcf))
        for cfg in self.config.get('apis', {}).values():
            self.apis.append(PyloneApi(cfg, gcf))

    def create_archi(self):
        for elem in [*self.layers, *self.functions, *self.apis]:
            if elem.cf.get('before-script'):
                run(elem.cf['before-script'])
            elem.create()
            if elem.cf.get('after-script'):
                run(elem.cf['after-script'])
        print(f'🚀 {self.config["name"]} hosted successfully')

    def delete_archi(self):
        for elem in [*self.apis, *self.functions, *self.layers]:
            elem.remove()
        print(f'🤯 {self.config["name"]} removed successfully')

    def update(self, stage):
        for elem in [*self.layers, *self.functions, *self.apis]:
            if self.options.force_update or elem.check_for_update(stage):
                if elem.cf.get('before-script'):
                    run(elem.cf['before-script'])
                elem.update(stage)
                if elem.cf.get('after-script'):
                    run(elem.cf['after-script'])
        print(f'🦄 {self.config["name"]} updated successfully')
