from .providers import providers
from .utils.scripts import run
from argparse import Namespace
from PyInquirer import prompt
from .questions import ask
from typing import List

from .functions import PyloneFct
from .layers import PyloneLayer
from .apis import PyloneApi


class PyloneProject():
    functions: List[PyloneFct] = list()
    layers: List[PyloneLayer] = list()
    apis: List[PyloneApi] = list()

    def __init__(self, options: Namespace, config):
        self.config = config
        self.options = options
        self.provider = providers[config['cloud']](config, options)
        self._init_classes()

    def inject_doppler_envs(self, cfg):
        if not self.options.doppler_token:
            return cfg

        if isinstance(cfg.get('environ'), dict):
            cfg['environ'] = {
                **cfg['environ'],
                **self.options.doppler_env
            }
        elif not cfg.get('environ'):
            cfg['environ'] = self.options.doppler_env
        return cfg

    def _init_classes(self):
        gcf = {
            'provider': self.provider,
        }
        for cfg in self.config.get('functions', {}).values():
            config = self.inject_doppler_envs(cfg)
            self.functions.append(PyloneFct(config, gcf))
        for cfg in self.config.get('layers', {}).values():
            self.layers.append(PyloneLayer(cfg, gcf))
        for cfg in self.config.get('apis', {}).values():
            self.apis.append(PyloneApi(cfg, gcf))
    
    def _get_objects(self):
        objects = [*self.layers, *self.functions, *self.apis]

        if self.options.objects:
            objects = list(filter(lambda x: x.cf['name'] in self.options.objects, objects))
        elif len(objects) > 1 and ask('Multiple objects detected, Choose what to update'):
            res = prompt({
                "type": "checkbox",
                "name": "objects",
                "choices": [{'name': obj.cf['name']} for obj in objects],
                "message": "Choose objects to update"
            })['objects']
            objects = list(filter(lambda x: x.cf['name'] in res, objects))

        if not objects:
            exit('Aborted, no objects to perform actions')

        return objects

    def create_archi(self):
        for elem in self._get_objects():
            if elem.cf.get('before-script'):
                run(elem.cf['before-script'])
            elem.create()
            if elem.cf.get('after-script'):
                run(elem.cf['after-script'])
        print(f'🚀 {self.config["name"]} hosted successfully')

    def delete_archi(self):
        for elem in self._get_objects():
            elem.remove()
        print(f'🤯 {self.config["name"]} removed successfully')

    def update(self, stage):
        for elem in self._get_objects():
            if self.options.force_update or elem.check_for_update(stage):
                if elem.cf.get('before-script'):
                    run(elem.cf['before-script'])
                elem.update(stage)
                if elem.cf.get('after-script'):
                    run(elem.cf['after-script'])
        print(f'🦄 {self.config["name"]} updated successfully')
