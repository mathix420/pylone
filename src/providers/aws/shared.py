import os
import json
import boto3

from ...questions import qload
from ...utils.gitignore import add_to_gitignore


def _init_creds(self):
    if os.path.exists(self.go.creds_path):
        with open(self.go.creds_path) as fp:
            j = json.load(fp)

        if 'aws' in j:
            self.creds = j['aws']
        else:
            self._create_creds()
    else:
        self._create_creds()


def _create_creds(self):
    self.creds = qload('credentials')
    with open(self.go.creds_path, 'w+') as fp:
        json.dump({'aws': self.creds}, fp)
    add_to_gitignore(self.go.creds_path.split('/')[-1])
