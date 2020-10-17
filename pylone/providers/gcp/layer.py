import os

def publish_layer(self, config):
    path = config.get('source', config['name'])

    if not os.path.exists(path):
        raise Exception(f"Error in {config['name']}, source do not exist!")
    else:
        code = self._send_to_s3(path, config)

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
    nx = 0
    layers = list()

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
            print('Error when deleting a version layer')
            print(e)
