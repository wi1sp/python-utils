from typing import Dict, List

from configs_to_format.configs_reader.config_directory_reader import ConfigDirectoryReader
from configs_to_format.formetter.base_formatter import BaseFormatter
from configs_to_format.processing.params import ProcessParams
from logger.logger_mixin import LoggerMixIn


class Processor(LoggerMixIn):
    def __init__(self, reader: ConfigDirectoryReader, formatter: BaseFormatter):
        self.reader = reader
        self.formatter = formatter

    def start(self, params: ProcessParams):
        result: List[Dict] = []

        for config in self.reader.read_configs_files(params.file_pattern):

            for data in params.config_structure.capture(config):
                result.append(data)

        self.formatter.write_to_format(result)
