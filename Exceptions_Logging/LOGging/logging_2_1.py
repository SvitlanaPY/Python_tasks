"""
Create root logger with configured logger level(DEBUG) but default handler(StreamHandler) in logging.basicConfig().
"""
import logging


logging.basicConfig(level='DEBUG')
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


def main(name):
    my_logger.debug(f"Enter in the main() function: name = {name}")
# DEBUG:root:Enter in the main() function: name = oleg   # root - імя дефолтного логера


if __name__ == '__main__':
    main('oleg')
