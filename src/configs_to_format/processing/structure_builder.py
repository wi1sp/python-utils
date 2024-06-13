from typing import Dict, List, Callable

from src.configs_to_format.config_structure.config_accessor import FromConfigAccessor
from src.configs_to_format.config_structure.config_field import ConfigField
from src.configs_to_format.config_structure.config_field_collection import ConfigFieldCollection
from src.configs_to_format.config_structure.multi_config_field import MultiConfigField


class StructureBuilder:
    def __init__(self, accessor_builder: Callable[[List[str]], FromConfigAccessor]):
        self.accessor_builder = accessor_builder

    def _build_on_depth(self, raw_structure: Dict) -> ConfigField:
        fields = []

        for tittle, options in raw_structure.items():
            if isinstance(options, dict):
                field = ConfigFieldCollection(
                    self._build_on_depth(options),
                    self.accessor_builder([tittle])
                )
                fields.append(field)
                continue

            field = ConfigField(name=tittle, accessor=self.accessor_builder(options))
            fields.append(field)

        return MultiConfigField(fields=fields, accessor=self.accessor_builder([]))

    def build(self, raw_structure: Dict) -> ConfigField:
        return self._build_on_depth(raw_structure)
