import datetime
from app.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from app import logger
from app.models.config import Config
from botocore.exceptions import ClientError, ParamValidationError


def _session() -> object:
    _session = Config(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    return _session.create_client()


class SsmCollect(object):

    def __init__(self):
        pass

    @staticmethod
    def _converter(_o: object) -> None:
        """Return str from datetime.
        :type _o: object
        """
        if isinstance(_o, datetime.datetime):
            return _o.__str__()
        return None

    @staticmethod
    def get_parameter(param_name: object) -> object:
        """Return the result of the boto3 ssm clients response.
        :type param_name: object
        """
        try:
            ssm_client = _session()
            parameter = ssm_client.get_parameter(
                Name=param_name, WithDecryption=True)
            return {
                'Name': parameter['Parameter']['Name'],
                'Value': parameter['Parameter']['Value'],
                'Version': parameter['Parameter']['Version'],
                'Modified': parameter['Parameter']['LastModifiedDate'].strftime('%Y-%m-%d'),
                'Arn': parameter['Parameter']['ARN'],
            }
        except ParamValidationError as _e:
            logger.error("Parameter validation error: %s" % _e)
        except ClientError as _e:
            logger.error("Unexpected error: %s" % _e)

    def get_parameters(self, res_type: object) -> dict:
        """Return the result of the boto3 ssm iterator clients response.
        get parameters, collect params which contain given string,
        put them into param_name list then call get_parameter() and
        put parameter value belongs to parameter_name
        :type res_type: object
        """
        ssm_client = _session()
        paginator = ssm_client.get_paginator('describe_parameters')
        params = []
        param_name = []
        param_value = dict()

        logger.info('P001-' + res_type)

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
