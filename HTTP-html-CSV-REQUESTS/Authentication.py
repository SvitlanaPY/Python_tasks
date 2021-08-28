import requests
from getpass import getpass

response = requests.get('https://github.com/', auth=('SvitlanaPY', getpass()))
# $Svetik13$
print(response.status_code)
