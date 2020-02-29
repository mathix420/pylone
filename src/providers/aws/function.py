import os
import boto3

def init_lambda(self):
    self.lb_client = boto3.client(
        'lambda',
        region_name=self.gb['region'],
        aws_access_key_id=self.creds['access_id'],
        aws_secret_access_key=self.creds['secret_key'],
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
        Publish=(stage != self.gb['stages'][0]),
    )
    self.lb_client.update_function_configuration(
        FunctionName=config['name'],
        Runtime=config.get('runtime', 'provided'),
        Role=config['role'],
        Handler=config['handler'],
        **others_configs
    )
    if stage == self.gb['stages'][0]:
        return
    self.lb_client.update_alias(
        Name=stage,
        FunctionName=config['name'],
        FunctionVersion=res['Version']
    )


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