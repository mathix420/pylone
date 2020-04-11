import os
import boto3
import shutil

from ...utils.checksum import md5_file
from botocore.client import ClientError


def init_s3(self):
    self.s3 = boto3.resource(
        's3',
        region_name=self.gb['region'],
        aws_access_key_id=self.creds['access_id'],
        aws_secret_access_key=self.creds['secret_key'],
    )


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
    key = md5_file('/tmp/update.zip')
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
