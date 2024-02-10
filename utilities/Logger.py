import logging
import inspect


class LoggenClass:
    @staticmethod
    def log_generator():
        log_name = inspect.stack()[1][3]  # runtime -getting filepath -class -method
        logger = logging.getLogger(log_name)  # gen logs
        logfile = logging.FileHandler("C:\\WebTesting\\LoginPage_Pytest\\Logs\\UserLog.log")  # log file
        log_format = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s ")  # log format
        logfile.setFormatter(log_format)  # setting format to the logs
        logger.addHandler(logfile)  # adding log everytime to same file
        logger.setLevel(logging.INFO)  # set log level
        return logger
