from abc import ABC, abstractmethod
from collections.abc import Iterator
from typing import List, Dict

from configs_to_format.config_structure.config_accessor import FromConfigAccessor
from configs_to_format.config_structure.config_field import ConfigField


class c(ConfigField):
    def __init__(self, fields: List[ConfigField], accessor: FromConfigAccessor):
        self.fields = fields
        super().__init__(self.__class__.__name__,  accessor)

    def capture(self, config) -> Iterator[Dict]:
        for group in self.accessor.get_from_config(config):
            result = {}

            for field in self.fields:
                result &= field.capture(group)

            yield group
