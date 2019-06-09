"""Class to handle boto3 session and client"""

import boto3
from botocore.exceptions import ClientError

from app import logger


class Config:
    
    def __init__(self, aws_access_key_id: str = '', aws_secret_access_key: str = ''):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key

    def create_client(self) -> object:
        """Creats the boto3 session and the client
        from the given parameters which are stored in
        the .env config file.
        :return: ssm_client: object
        """
        try:
            session = boto3.session.Session(self.aws_access_key_id,
                                            self.aws_secret_access_key)
            ssm_client = session.client('ssm')
            return ssm_client

        except ClientError as _e:
            logger.error("Unexpected error: %s" % _e)
