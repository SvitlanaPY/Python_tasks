"""
Create root logger and change logger level using setLevel().
"""
import logging

# logging.basicConfig(level='DEBUG')
my_logger = logging.getLogger()
print("my_logger: ", my_logger)
# my_logger:  <RootLogger root (DEBUG)>
print("my_logger.level: ", my_logger.level)
# my_logger.level:  30
print()

# my_logger.setLevel('DEBUG')
my_logger.setLevel(10)
print("my_logger_changed_level: ", my_logger.level)
# my_logger.level:  10
print()

print("my_logger.handlers: ", my_logger.handlers)
# my_logger.handlers:  [<StreamHandler <stderr> (NOTSET)>]
print()


def main(name):
    my_logger.debug(f"MSG: Enter in the main() function: name = {name}")
#   у момент виклику метода warning(), логер створив екземпляр класу LogRecord
# DEBUG:root:Enter in the main() function: name = oleg   # root - імя дефолтного логера

if __name__ == '__main__':
    main('oleg')
