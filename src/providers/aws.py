import os
import json
import boto3

from ..questions import qload


class AWSProvider():
    creds = dict()
    lambda_role = None

    def __init__(self, global_config):
        self._init_creds()
        self.lb_client = boto3.client(
            'lambda',
            region_name=global_config['region'],
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

    def _create_lambda_role(self):
        # TODO:
        return "arn:aws:iam::394115634019:role/dev-GraphQLRole-1EHEIW52JVMUS"

    def _send_to_s3(self, path):
        # TODO:
        return {
            'S3Bucket': 'lambda-graphql-api',
            'S3Key': 'ede21c4a438f02a69543e59d12ee5f93'
        }

    def create_function(self, config):
        path = config.get('source', config['name'])

        if not config.get('role'):
            config['role'] = self.lambda_role or self._create_lambda_role()
        if not os.path.isdir(path):
            raise Exception(f"Error in {config['name']}, source do not exist!")
        else:
            code = self._send_to_s3(path)

        others_configs = {
            k: v for k, v in {
                'Description': config.get('description'),
                'Timeout': config.get('timeout'),
                'MemorySize': config.get('memory'),
                'VpcConfig': config.get('vpc'),
                'Environment': config.get('environ'),
                'Layers': config.get('layers')
            }.items() if v
        }

        return self.lb_client.create_function(
            FunctionName=config['name'],
            Runtime=config.get('runtime', 'provided'),
            Role=config['role'],
            Handler=config['handler'],
            Code=code,
            Publish=config.get('publish', False),
            **others_configs
        )['FunctionArn']

    def delete_function(self, config):
        return self.lb_client.delete_function(
            FunctionName=config['name'],
        )

    def update_function(self, config, stage):
        path = config.get('source', config['name'])
        # TODO: stage
        if not config.get('role'):
            config['role'] = self.lambda_role or self._create_lambda_role()
        if not os.path.isdir(path):
            raise Exception(f"Error in {config['name']}, source do not exist!")
        else:
            code = self._send_to_s3(path)

        others_configs = {
            k: v for k, v in {
                'Description': config.get('description'),
                'Timeout': config.get('timeout'),
                'MemorySize': config.get('memory'),
                'VpcConfig': config.get('vpc'),
                'Environment': config.get('environ'),
                'Layers': config.get('layers')
            }.items() if v
        }
        self.lb_client.update_function_code(
            FunctionName=config['name'],
            **code,
            Publish=config.get('publish', False),
        )
        return self.lb_client.update_function_configuration(
            FunctionName=config['name'],
            Runtime=config.get('runtime', 'provided'),
            Role=config['role'],
            Handler=config['handler'],
            **others_configs
        )

    def publish_layer(self, config):
        path = config.get('source', config['name'])

        if not os.path.isdir(path):
            raise Exception(f"Error in {config['name']}, source do not exist!")
        else:
            code = self._send_to_s3(path)

        others_configs = {
            k: v for k, v in {
                'Description': config.get('description'),
                'LicenseInfo': config.get('licenseInfo'),
                'MemorySize': config.get('memory'),
                'VpcConfig': config.get('vpc'),
                'Environment': config.get('environ'),
            }.items() if v
        }

        return self.lb_client.publish_layer_version(
            LayerName=config['name'],
            Content=code,
            CompatibleRuntimes=config['runtimes'],
            **others_configs
        )['LayerVersionArn']

    def delete_layer(self, config):
        layers = list()
        nx = 0
        while nx or nx == 0:
            marker = {'Marker': nx} if nx else dict()
            res = self.lb_client.list_layer_versions(
                LayerName=config['name'],
                MaxItems=50,
                **marker
            )
            nx = res.get('NextMarker')
            layers += res.get('LayerVersions', [])
        for layer in layers:
            try:
                self.lb_client.delete_layer_version(
                    LayerName=config['name'],
                    VersionNumber=layer['Version']
                )
            except Exception as e:
                print(e)
