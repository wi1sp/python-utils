import yaml

from configs_to_format.configs_reader.config_reader import ConfigReader


class YamlConfigReader(ConfigReader):
    def read_from_path(self, file_path: str):
        with open(file_path, encoding='utf-8') as file:
            configuration = yaml.safe_load(file)

        return configuration
