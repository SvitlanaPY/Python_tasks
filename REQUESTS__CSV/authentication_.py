import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

response = requests.get('https://github.com/', auth=HTTPBasicAuth('SvitlanaPY', '$Svetik13$'))
print(response.status_code)


response = requests.get('https://github.com/', auth=('SvitlanaPY', getpass()))
# $Svetik13$
print(response.status_code)
