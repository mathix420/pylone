from botocore.exceptions import ClientError


class PyloneFct():
    def __init__(self, config, global_config):
        self.cf = config
        self.provider = global_config['provider']

    def check_for_update(self, stage):
        # TODO:
        return True

    def update(self, stage):
        self.provider.update_function(self.cf, stage)

    def create(self):
        self.provider.create_function(self.cf)

    def remove(self):
        try:
            self.provider.delete_function(self.cf)
        except ClientError as e:
            if e.response['Error']['Code'] == 'ResourceNotFoundException':
                print('Ressource do not exist')
            else:
                raise
