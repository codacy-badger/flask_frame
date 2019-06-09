import requests
from app.settings import API_URL
from app import logger


class ApiCall:

    def __init__(self):
        pass

    @staticmethod
    def get(route_url, params=None):
        if params is None:
            params = {}
        url = API_URL + route_url
        logger.debug('PU001 - URL to collect all item' + url)
        return requests.get(url, params=params).json()

    @staticmethod
    def get_id(route_url, sid, params=None):

        if params is None:
            params = {}
        url = API_URL + route_url + sid

        logger.debug('PU002 - URL to collect item per ID' + url)
        logger.info(requests.get(url, params=params).json())

        return [requests.get(url, params=params).json()]

"""
    def post(self, route_url, params = {}):
        url = api_url + route_url
        params['access_token']  = self.access_token

        return requests.post(url, params=params).json()

    def delete(self, route_url, params = {}):
        url = api_url + route_url
        params['access_token']  = self.access_token

        return requests.delete(url, params=params)

    @staticmethod
    def get_user_from_token(access_token):
        #Fetch user data using the access token.
        url = api_url + '/user'
        params = { 'access_token': access_token }

        return requests.get(url, params=params).json()
"""