import requests
import configparser
from Utilities.resources import ApiResources

from Utilities.configuration import *

config=configparser.ConfigParser()
config.read('Utilities/properties.ini')
print(config['API']['Endpoint'])
# response=requests.get(url,params={'AuthorName':'Rahul Shetty'},)

# print(response.json())