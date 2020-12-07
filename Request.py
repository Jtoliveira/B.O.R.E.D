import requests

class Request:
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl

    def makeRequest(self,parameters):
        print(self.baseUrl + "?" + parameters)
        return requests.get(self.baseUrl + "?" + parameters).json()