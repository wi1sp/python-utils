from abc import ABC, abstractmethod
from typing import List, Dict


class BaseFormatter(ABC):
    @abstractmethod
    def write_to_format(self, records: List[Dict]):
        raise NotImplementedError()
