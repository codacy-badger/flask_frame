import requests
from app.settings import API_URL
from app import logger


class ApiCall():

    def __init__(self):
        pass

    def get(self, route_url, params = {}):
        url = API_URL + route_url
        logger.debug('PU001 - URL to collect all item' + url)
        return requests.get(url, params=params).json()

    def get_id(self, route_url, id, params = {}):

        url = API_URL + route_url + id

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