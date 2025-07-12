# logger.py
import logging

def setup_logger():
    logger = logging.getLogger("TradingBot")
    # set's logging level to info
    logger.setLevel(logging.INFO)
    # Written logs to file bot.log
    fh = logging.FileHandler("bot.log")
    # Define Fortmat each log entry
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    # Applies format 
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
