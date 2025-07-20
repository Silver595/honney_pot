import logging
from logging.handlers import RotatingFileHandler

logging_format = logging.Formatter('%(message)s')

funnal_logger = logging.getLogger('funnelLogger')
funnal_logger.setLevel(logging.INFO)
funnal_handler = RotatingFileHandler('audits.log',maxBytes=2000,backupCount=5)
funnal_handler.setFormatter(logging_format)
funnal_logger.addHandler(funnal_handler)
