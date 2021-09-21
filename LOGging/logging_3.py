import logging
import requests


logging.basicConfig(level='DEBUG')
my_logger = logging.getLogger()
# print("my_logger.handlers: ", my_logger.handlers)   # my_logger.handlers:  [<StreamHandler <stderr> (NOTSET)>]


def main(name):
    my_logger.debug(f"Enter in the main() function: name = {name}")
    r = requests.get('https://www.google.ru')   # запит до сервера гугла
# будемо бачити ВСІ повідомлення рівня DEBUG, які були використані в проекті
# (бібліотека urllib3 теж створила повідомлення рівня DEBUG всередині модуля requests)

# DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): www.google.ru:443
# DEBUG:urllib3.connectionpool:https://www.google.ru:443 "GET / HTTP/1.1" 200 None
# DEBUG:root:Enter in the main() function: name = oleg     # root - імя дефолтного логера

# модуль logging реалізує паттерн singletone: це глобальний модуль для всього нашого проекту, логери - вони глобальні
# і ф-ія basicConfig() створює глобальні налаштування для всіх модулів проекту (любий логер має своїм предком root-логера)
# logging.getLogger('urllib3').setLevel('CRITICAL')    # щоб виключити DEBUG:urllib3 логи
# які ж логери були використані в нашому проекті?:
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
#
# бібліотека requests працює поверх бібліотеки urllib3
# отримуємо логер з іменем urllib3:
# print(logging.getLogger('urllib3'))   # <Logger urllib3 (DEBUG)>
#
# змінюємо для логера з іменем urllib3 рівень повідомлень (відфільтровуємо повідомлення для ін логерів в проекті):
# logging.getLogger('urllib3').setLevel('CRITICAL')    # щоб виключити DEBUG:urllib3 логи
print()


if __name__ == '__main__':
    main('oleg')
