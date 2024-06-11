from typing import Dict, List

from configs_to_format.configs_reader.config_directory_reader import ConfigDirectoryReader
from configs_to_format.processing.params import ProcessParams


class Processor:
    def __init__(self, reader: ConfigDirectoryReader):
        self.reader = reader

    def start(self, params: ProcessParams):
        result: List[Dict] = []

        for config in self.reader.read_configs_files(params.file_pattern):
            parse_stack = [params.config_structure[0].capture(config)]
            config_result = []

            while parse_stack:
                item = next(parse_stack[-1], None)

                if item is None:
                    parse_stack.pop()
                    config_result.pop()
                    continue

                config_result.append(item)

                if len(config_result) == len(params.config_structure):
                    parse_result = {}
                    for fields in config_result:
                        parse_result.update(fields)

                    result.append(parse_result)
                    config_result.pop()
                    continue

                level = len(parse_stack)
                parse_stack.append(params.config_structure[level].capture(config))
