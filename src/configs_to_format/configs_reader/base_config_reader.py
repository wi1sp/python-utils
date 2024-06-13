from abc import ABC, abstractmethod


class BaseConfigReader(ABC):
    @abstractmethod
    def read_from_path(self, file_path: str):
        raise NotImplementedError()
