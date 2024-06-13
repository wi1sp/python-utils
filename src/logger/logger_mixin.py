import logging
from abc import ABC
from functools import cached_property


class LoggerMixIn(ABC):
    @staticmethod
    def init_logger(name: str) -> logging.Logger:
        logger = logging.getLogger(f"cli.utils.{name}" if name is not None else 'cli.utils')
        return logger

    @cached_property
    def logger(self):
        return self.init_logger(self.__class__.__module__)
