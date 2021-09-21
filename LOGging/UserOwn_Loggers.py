import logging
# Create a custom logger
my_logger = logging.getLogger(<name>)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')

# Set logs' level:
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
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

