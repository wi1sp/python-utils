from collections.abc import Iterator
from typing import List, Dict

from .config_accessor import  FromConfigAccessor
from .config_field import ConfigField


class MultiConfigField(ConfigField):
    def __init__(self, fields: List[ConfigField], accessor: FromConfigAccessor):
        self.fields = fields
        super().__init__(self.__class__.__name__,  accessor)

    def capture(self, config) -> Iterator[Dict]:
        parse_stack = [self.fields[0].capture(self.accessor.get_from_config(config))]
        config_result = []

        while parse_stack:
            item = next(parse_stack[-1], None)

            if item is None:
                parse_stack.pop()
                if config_result:
                    config_result.pop()
                continue

            config_result.append(item)

            if len(config_result) == len(self.fields):
                parse_result = {}
                for fields in config_result:
                    parse_result.update(fields)

                yield parse_result
                config_result.pop()
                continue

            level = len(parse_stack)
            parse_stack.append(self.fields[level].capture(self.accessor.get_from_config(config)))
