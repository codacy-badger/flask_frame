import boto3
import configparser
from botocore.exceptions import ClientError, ParamValidationError

from app import logger

class Config():

    def __init__(self, profile_name='', region_name=''):
        self.profile_name = profile_name
        self.region_name = region_name

    def create_client(self,) -> object:
        CONFIG = configparser.ConfigParser()
        CONFIG.read('../../config.ini')
        PROFILE_NAME = CONFIG['GLOBAL']['PROFILE_NAME']
        REGION_NAME = CONFIG['GLOBAL']['REGION_NAME']

        try:
            session = boto3.session.Session(profile_name=PROFILE_NAME,
                                            region_name=REGION_NAME)
            ssm_client = session.client('ssm')
            return ssm_client

        except ClientError as _e:
            logger.error("Unexpected error: %s" % _e)