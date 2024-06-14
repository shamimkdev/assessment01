from loguru import logger
from datetime import datetime

logger.add("logs/app.log", rotation="500 MB")

def log_info(message: str):
    logger.info(message)

def log_error(message: str):
    logger.error(message)
