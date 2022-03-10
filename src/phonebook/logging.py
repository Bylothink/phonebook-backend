import logging

CRITICAL = logging.CRITICAL
ERROR = logging.ERROR
WARNING = logging.WARNING
INFO = logging.INFO
DEBUG = logging.DEBUG
NOTSET = logging.NOTSET

getLogger = logging.getLogger


class StdLogger(logging.Logger):
    def __init__(self, name, level=None):
        if not level:
            level = INFO

        super().__init__(name, level)

        handler = logging.StreamHandler()
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s (%(name)s on %(threadName)s): %(message)s')

        handler.setFormatter(formatter)
        self.addHandler(handler)


logging.setLoggerClass(StdLogger)
