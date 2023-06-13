import configparser
def getconfig():
    config=configparser.ConfigParser()
    config.read('Utilities/properties.ini')
    print(config['API']['Endpoint'])
    return config

