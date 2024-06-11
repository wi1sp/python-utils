from abc import ABC, abstractmethod
from typing import Dict, Iterator

from configs_to_format.config_structure.config_accessor import FromConfigAccessor


class ConfigField:
    def __init__(self, name, accessor: FromConfigAccessor):
        self.name = name
        self.accessor = accessor

    def capture(self, config) -> Iterator[Dict]:
        yield {self.name: self.accessor.get_from_config(config)}
