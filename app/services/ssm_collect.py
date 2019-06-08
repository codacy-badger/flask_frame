import datetime
import json
import boto3
from app import logger
from botocore.exceptions import ClientError, ParamValidationError

PROFILE_NAME = 'dev'
REGION_NAME = 'eu-west-1'


class SsmCollect(object):

    def __init__(self):
        pass

    def _converter(self, _o: object) -> str:
        """Return str from datetime.
        :type _o: object
        """
        if isinstance(_o, datetime.datetime):
            return _o.__str__()
        return None

    def get_parameter(self, param_name: object) -> object:
        """Return the result of the boto3 ssm clients response.
        :type param_name: object
        """
        try:
            session = boto3.session.Session(profile_name=PROFILE_NAME,
                                            region_name=REGION_NAME)
            ssm_client = session.client('ssm')
            parameter = ssm_client.get_parameter(
                Name=param_name, WithDecryption=True)
            return {
            'Name': parameter['Parameter']['Name'],
            'Value': parameter['Parameter']['Value'],
            'Version': parameter['Parameter']['Version'],
            'Modified': parameter['Parameter']['LastModifiedDate'],
            'Arn': parameter['Parameter']['ARN'],
            }
        except ParamValidationError as _e:
            logger("Parameter validation error: %s" % _e)
        except ClientError as _e:
            logger("Unexpected error: %s" % _e)

    def get_parameters(self, res_type: object) -> dict:
        """Return the result of the boto3 ssm iterator clients response.
        get parameters, collect params which contain given string,
        put them into param_name list then call get_parameter() and
        put parameter value belongs to parameter_name
        :type res_type: object
        """
        session = boto3.session.Session(profile_name=PROFILE_NAME,
                                        region_name=REGION_NAME)
        ssm_client = session.client('ssm')
        paginator = ssm_client.get_paginator('describe_parameters')
        params = []
        param_name = []
        param_value = dict()

        for response in paginator.paginate():
            params.append(response['Parameters'])

        for iteration, _ in enumerate(params):
            for param_obj, _ in enumerate(params[iteration]):
                if res_type in params[iteration][param_obj]['Name']:
                    param_name.append((params[iteration][param_obj]['Name']))

        for iteration, _ in enumerate(param_name):
            # TODO create list from these objects
            param_value.update({iteration: self.get_parameter(param_name[iteration])})

        return param_value
