import logging


logging.basicConfig(level='DEBUG')
# my_logger.setLevel('DEBUG')
# my_logger.setLevel(10)
# my_logger.setLevel(logging.debug())
my_logger = logging.getLogger()
print("my_logger: ", my_logger)
# my_logger:  <RootLogger root (DEBUG)>
print()
print("my_logger.level: ", my_logger.level)
# my_logger.level:  10
print()
print("my_logger.handlers: ", my_logger.handlers)
# my_logger.handlers:  [<StreamHandler <stderr> (NOTSET)>]
print()
# logging.basicConfig(level='DEBUG', filename='mylog.log')
# print("my_logger.handlers: ", my_logger.handlers)
# [<FileHandler /home/svitlana/Projects/Python_Tasks/LOGging/mylog.log (NOTSET)>]


def main(name):
    my_logger.debug(f"Enter in the main() function: name = {name}")
# DEBUG:root:Enter in the main() function: name = oleg   # root - імя дефолтного логера


if __name__ == '__main__':
    main('oleg')
