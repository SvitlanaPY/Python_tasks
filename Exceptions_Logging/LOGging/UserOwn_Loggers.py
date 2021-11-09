import logging

# Create a custom LOGGER:
my_logger = logging.getLogger(__name__)
print("logger level BEFORE:", my_logger.level)   # logger level BEFORE: 0

# # How to set logs' LEVEL for LOGGER':
# my_logger.setLevel(10)
# print("logger level AFTER:", my_logger.level)   # logger level AFTER: 10

# Create HANDLERs:
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
# print("c_handler level BEFORE: ", c_handler.level)   # c_handler level BEFORE:  0
# print("f_handler level BEFORE: ", f_handler.level)   # f_handler level BEFORE:  0


# Set logs' LEVEL (for handlers'):
c_handler.setLevel(logging.WARNING)   # c_handler.setLevel('WARNING');  # c_handler.setLevel(30)
f_handler.setLevel(logging.ERROR)
# print("c_handler level AFTER: ", c_handler.level)   # c_handler level AFTER:  30
# print("f_handler level AFTER: ", f_handler.level)   # f_handler level AFTER:  40

# Create FORMATTERs (для хендлерів):
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# set FORMATTERs to HANDLERs:
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# add HANDLERs to LOGGER:
my_logger.addHandler(c_handler)
my_logger.addHandler(f_handler)

# команди на запис в лог
my_logger.debug("debug msg")
# logging.debug("debug msg")
my_logger.info("info msg")
my_logger.warning("warning msg")
my_logger.error("error msg")
# logging.error("error msg")
my_logger.critical("critical msg")

# ми створили ОДИН логер my_logger і два його хендлери: c_handler та f_handler
# c_handler - виводить повідомлення рівня WARNING і вище (30-WARNING, 40-ERROR, та 50-CRITICAL) у консоль,
# f_handler - виводить повідомлення рівня ERROR та вище (40-ERROR, та 50-CRITICAL) у лог-файл 'file.log'
