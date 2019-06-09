import boto3
from botocore.exceptions import ClientError

from app import logger

class Config():

    def __init__(self, aws_access_key_id='', aws_secret_access_key=''):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key

    def create_client(self) -> object:

        try:
            session = boto3.session.Session(self.aws_access_key_id,
                                            self.aws_secret_access_key)
            ssm_client = session.client('ssm')
            return ssm_client

        except ClientError as _e:
            logger.error("Unexpected error: %s" % _e)
