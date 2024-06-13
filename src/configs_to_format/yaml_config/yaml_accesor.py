from typing import List, Any

from src.configs_to_format.config_structure.config_accessor import FromConfigAccessor


class YamlConfigAccessor(FromConfigAccessor):
    def __init__(self, path: List[str]):
        self.path = path

    def get_from_config(self, config) -> Any:
        result = config
        for key in self.path:
            result = result[key]

        return result
