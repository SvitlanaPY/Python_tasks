import pprint
import logging
import requests


logging.basicConfig(level='DEBUG')
my_logger = logging.getLogger()
print("my_logger.handlers: ", my_logger.handlers)
# my_logger.handlers:  [<StreamHandler <stderr> (NOTSET)>]  # StreamHandler виводить логи в консоль

print()
print(logging.getLogger('urllib3'))   # <Logger urllib3 (DEBUG)>
# logging.getLogger('urllib3').setLevel('CRITICAL')    # щоб виключити DEBUG:urllib3 логи
print()


for key in logging.Logger.manager.loggerDict:
    print(key)
# urllib3.util.retry
# urllib3.util
# urllib3
# urllib3.connection
# urllib3.response
# urllib3.connectionpool
# urllib3.poolmanager
# requests


def main(name):
    my_logger.debug(f"Enter in the main() function: name = {name}")
    r = requests.get('https://www.google.ru')

# DEBUG:root:Enter in the main() function: name = oleg   # root - імя дефолтного логера


# логи з urllib3/requests
# DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): www.google.ru:443
# DEBUG:urllib3.connectionpool:https://www.google.ru:443 "GET / HTTP/1.1" 200 None

# logging.getLogger('urllib3').setLevel('CRITICAL')    # щоб виключити DEBUG:urllib3 логи


if __name__ == '__main__':
    main('oleg')
