import logging

# Create a custom LOGGER:
my_logger = logging.getLogger(__name__)

# Create HANDLERs:
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')

# Set logs' level (for handlers'):
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create FORMATTERs для хендлерів:
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add FORMATTERs to HANDLERs:
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
my_logger.addHandler(c_handler)
my_logger.addHandler(f_handler)

# команди на запис в лог
my_logger.debug("debug msg")
my_logger.info("info msg")
my_logger.warning("warning msg")
my_logger.error("error msg")
my_logger.critical("critical msg")

# ми створили ОДИН логер і два його хендлери: c_handler та f_handler
# c_handler - виводить повідомлення рівня WARNING і вище (30-WARNING, 40-ERROR, та 50-CRITICAL) у консоль,
# а f_handler - виводить повідомлення рівня ERROR та вище (40-ERROR, та 50-CRITICAL) у лог-файл 'file.log'
