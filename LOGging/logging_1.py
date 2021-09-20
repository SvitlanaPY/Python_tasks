import pprint
import logging


my_logger = logging.getLogger()
# ф-ія getLogger() приймає один параметр - name, імя логера.
# Якщо у фі-ю getLogger() НЕ передано імені, то вона створює root-логер по замовчуванню.
print("my_logger: ", my_logger)
# <RootLogger root (WARNING)>
print()

# pprint.pprint(dir(my_logger))


# по замовчуванню об"єкти root-логера мають рівень 30-WARNING
# отже, всі повідомлення, які менш важливі (10- та 20- логер НЕ буде обробляти,
# тобто ці повідомлення НЕ будуть доходити до хендлера)
print("my_logger.level: ", my_logger.level)
# my_logger.level:  30

# можна міняти рівень повідомлень кореневого-логера за допомогою ф-ії/метода setLevel():
# my_logger.setLevel('DEBUG')
# або
# my_logger.setLevel(10)
# або
# my_logger.setLevel(logging.debug())
# АЛЕ рівень повідомлень хендлера НЕ буде змінюватись;
# потрібно додатково при потребі змінювати рівень повідомлень для хендлера тією ж ф-ією


print()
print("my_logger.handlers: ", my_logger.handlers)
# []
# для НЕсконфігурованого root-логера, створюється хендлер типу StreamHandler з рівнем повідомлень 0-NOTSET,
# але він НЕ закріплюється за root-логером і тому ліст порожній... - []
print()
# для конфігурації root-логера в модулі logging є ф-ія basicConfig()
# в basicConfig() можна задавати рівень повідомлень для root-логера і для його хендлера:
# logging.basicConfig(level='DEBUG', filename="mylog.log")
# logging.basicConfig(level=logging.DEBUG, filename="mylog.log")
# logging.basicConfig(level=10, filename="mylog.log")
# print("my_logger.handlers: ", my_logger.handlers)
# [<FileHandler /home/svitlana/Projects/Python_Tasks/LOGging/mylog.log (NOTSET)>]


def main(name):
    my_logger.warning(f"Enter in the main() function: name = {name}")

# DEBUG:root:Enter in the main() function: name = oleg   # root - імя дефолтного логера


if __name__ == '__main__':
    main('oleg')