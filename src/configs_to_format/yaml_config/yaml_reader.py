import yaml

from src.configs_to_format.configs_reader.base_config_reader import BaseConfigReader


class YamlConfigReader(BaseConfigReader):
    def read_from_path(self, file_path: str):
        with open(file_path, encoding='utf-8') as file:
            configuration = yaml.safe_load(file)

        return configuration
