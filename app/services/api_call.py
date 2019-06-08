import requests, json
from app import logger
api_url = 'https://px84fa2qwe.execute-api.eu-west-1.amazonaws.com/dev'


class ApiCall():

    def __init__(self):
        pass

    def get(self, route_url, params = {}):
        url = api_url + route_url
        logger.log(url)
        return requests.get(url, params=params).json()

    def get_id(self, route_url, id, params = {}):
        url = api_url + route_url + id
        logger.log(requests.get(url, params=params).json())
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