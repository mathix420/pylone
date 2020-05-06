import boto3

from .function import init_lambda
from .iam import init_iam
from .s3 import init_s3

inits = [
    init_lambda,
    init_iam,
    init_s3,
]


class AWSProvider():
    creds = dict()
    lambda_role = None

    from .shared import _create_creds, _init_creds

    def __init__(self, global_config, options):
        """
        gb => pylone.yaml
        go => CLI params
        """
        self.gb = global_config
        self.go = options
        self._init_creds()
        for init in inits:
            init(self)

    from .function import create_function, delete_function, update_function
    from .layer import delete_layer, publish_layer
    from .s3 import _bucket_exist, _send_to_s3
    from .iam import _create_lambda_role
