from loguru import logger

class Logger():
    def __init__(self):
        self.log = logger
        self.log.add("./logs/{time: YYYY-MM-DD}.log", rotation="10 MB")

    def info(self, s):
        self.log.info(s)

    def warning(self, s):
        self.log.warning(s)

    def debug(self, s):
        self.log.debug(s)

    def error(self, s):
        self.log.error(s)

    def exception(self, s):
        self.log.exception(s)

_logger = Logger()