from botocore.exceptions import ClientError


class PyloneLayer():
    def __init__(self, config, global_config):
        self.cf = config
        self.provider = global_config['provider']

    def check_for_update(self, stage):
        # TODO:
        return True

    def update(self, stage):
        self.provider.publish_layer(self.cf)

    def create(self):
        self.provider.publish_layer(self.cf)

    def remove(self):
        try:
            self.provider.delete_layer(self.cf)
        except ClientError as e:
            if e.response['Error']['Code'] == 'ResourceNotFoundException':
                print('Ressource do not exist')
            else:
                raise