from abc import ABC, abstractmethod
from typing import Any


class FromConfigAccessor(ABC):
    @abstractmethod
    def get_from_config(self, config) -> Any:
        return config
