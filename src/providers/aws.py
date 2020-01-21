import os
import json
import boto3

from ..questions import qload


class AWSProvider():
    creds = dict()

    def __init__(self, global_config):
        self._init_creds()
        self.client = boto3.client(
            'lambda',
            aws_access_key_id=self.creds['access_id'],
            aws_secret_access_key=self.creds['secret_key'],
        )

    def _init_creds(self):
        if not os.path.exists('.creds'):
            self._create_creds()
        else:
            with open('.creds') as fp:
                j = json.load(fp)

            if 'aws' in j:
                self.creds = j['aws']
            else:
                self._create_creds()

    def _create_creds(self):
        self.creds = qload('credentials')
        with open('.creds', 'w+') as fp:
            json.dump({'aws': self.creds}, fp)

    def push_function(self, name, config):
        self.client.update_function_configuration(
            'deded',
            FunctionName=name,
        )
