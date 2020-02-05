import datetime
import shutil
import boto3
import json
import os

from ..questions import qload
from ..utils.checksum import gen_sum
from botocore.client import ClientError


class AWSProvider():
    creds = dict()
    lambda_role = None

    def __init__(self, global_config, options):
        self.gb = global_config
        self.go = options
        self._init_creds()
        self.lb_client = boto3.client(
            'lambda',
            region_name=global_config['region'],
            aws_access_key_id=self.creds['access_id'],
            aws_secret_access_key=self.creds['secret_key'],
        )
        self.s3 = boto3.resource(
            's3',
            region_name=global_config['region'],
            aws_access_key_id=self.creds['access_id'],
            aws_secret_access_key=self.creds['secret_key'],
        )

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

    def _create_lambda_role(self):
        # TODO:
        return "arn:aws:iam::394115634019:role/dev-GraphQLRole-1EHEIW52JVMUS"

    def _bucket_exist(self, bucket):
        try:
            self.s3.meta.client.head_bucket(Bucket=bucket)
        except ClientError:
            return False
        return True

    def _send_to_s3(self, path):
        if '.zip' in path:
            shutil.move(path, '/tmp/update.zip')
        else:
            shutil.make_archive('/tmp/update', 'zip', path)
        key = gen_sum('/tmp/update.zip')
        if not self._bucket_exist('pylone-bucket'):
            self.s3.create_bucket(
                Bucket='pylone-bucket',
                CreateBucketConfiguration={
                    'LocationConstraint': self.gb['region']
                }
            )
        self.s3.meta.client.upload_file(
            '/tmp/update.zip',
            'pylone-bucket',
            key,
        )
        return {
            'S3Bucket': 'pylone-bucket',
            'S3Key': key
        }

    def create_function(self, config):
        path = config.get('source', config['name'])

        if not config.get('role'):
            config['role'] = self.lambda_role or self._create_lambda_role()
        if not os.path.exists(path):
            raise Exception(f"Error in {config['name']}, source do not exist!")
        else:
            code = self._send_to_s3(path)

        others_configs = {
            k: v for k, v in {
                'Description': config.get('description'),
                'Timeout': config.get('timeout'),
                'MemorySize': config.get('memory'),
                'VpcConfig': config.get('vpc'),
                'Layers': config.get('layers')
            }.items() if v
        }
        if config.get('environ'):
            others_configs['Environment'] = {
                'Variables': config['environ']
            }

        arn = self.lb_client.create_function(
            FunctionName=config['name'],
            Runtime=config.get('runtime', 'provided'),
            Role=config['role'],
            Handler=config['handler'],
            Code=code,
            Publish=config.get('publish', False),
            **others_configs
        )['FunctionArn']

        for stage in self.gb['stages']:
            self.lb_client.create_alias(
                Name=stage,
                FunctionName=arn,
                FunctionVersion='$LATEST',
                Description=f'{stage} grade function'
            )

    def delete_function(self, config):
        return self.lb_client.delete_function(
            FunctionName=config['name'],
        )

    def update_function(self, config, stage):
        path = config.get('source', config['name'])
        # TODO: stage
        if not config.get('role'):
            config['role'] = self.lambda_role or self._create_lambda_role()
        if not os.path.exists(path):
            raise Exception(f"Error in {config['name']}, source do not exist!")
        else:
            code = self._send_to_s3(path)

        others_configs = {
            k: v for k, v in {
                'Description': config.get('description'),
                'Timeout': config.get('timeout'),
                'MemorySize': config.get('memory'),
                'VpcConfig': config.get('vpc'),
                'Layers': config.get('layers')
            }.items() if v
        }
        if config.get('environ'):
            others_configs['Environment'] = {
                'Variables': config['environ']
            }

        res = self.lb_client.update_function_code(
            FunctionName=config['name'],
            **code,
            Publish=(stage == 'prod'),
        )
        self.lb_client.update_function_configuration(
            FunctionName=config['name'],
            Runtime=config.get('runtime', 'provided'),
            Role=config['role'],
            Handler=config['handler'],
            **others_configs
        )
        if stage == 'dev':
            return
        self.lb_client.update_alias(
            Name=stage,
            FunctionName=config['name'],
            FunctionVersion=res['Version']
        )

    def publish_layer(self, config):
        path = config.get('source', config['name'])

        if not os.path.exists(path):
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
