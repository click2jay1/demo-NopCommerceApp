import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        return config.get('URL info', 'base_url')

    @staticmethod
    def getUsername():
        return config.get('Credentials info', 'username')

    @staticmethod
    def getPassword():
        return config.get('Credentials info', 'password')