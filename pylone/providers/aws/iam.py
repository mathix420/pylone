import boto3

def init_iam(self):
    self.iam = boto3.client(
        'iam',
        region_name=self.gb['region'],
        aws_access_key_id=self.creds['access_id'],
        aws_secret_access_key=self.creds['secret_key'],
    )

def _create_lambda_role(self):
    # TODO:
    return "arn:aws:iam::394115634019:role/dev-GraphQLRole-1EHEIW52JVMUS"
