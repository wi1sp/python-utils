from typing import Iterator, Dict

from configs_to_format.config_structure.config_accessor import FromConfigAccessor
from configs_to_format.config_structure.config_field import ConfigField


class ConfigFieldCollection(ConfigField):
    def __init__(self, field: ConfigField, accessor: FromConfigAccessor):
        super().__init__(ConfigFieldCollection.__name__, accessor)
        self.field = field

    def capture(self, config) -> Iterator[Dict]:
        for group in self.accessor.get_from_config(config):
            yield from self.field.capture(group)
