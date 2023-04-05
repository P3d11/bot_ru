import json


class Credential:
    """Class to store array of credentials for the application"""

    def __init__(self, credentialsFile):
        self.__credentials = self.__parseCredentials(credentialsFile)

    def __parseCredentials(self, credentialsFile):
        """Parses the credentials file and returns a list of credentials"""
        with open(credentialsFile) as f:
            file = json.load(f)
        return file['credentials']

    def getCredentials(self):
        """Returns the credentials"""
        return self.__credentials
