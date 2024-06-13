from typing import Dict, List

from src.configs_to_format.configs_reader.config_directory_reader import ConfigDirectoryReader
from src.configs_to_format.formetter.base_formatter import BaseFormatter
from src.configs_to_format.formetter.to_excel_formatter import ToExcelFormatter
from src.configs_to_format.processing.params import ProcessParams
from src.configs_to_format.processing.structure_builder import StructureBuilder
from src.configs_to_format.yaml_config.yaml_accesor import YamlConfigAccessor
from src.configs_to_format.yaml_config.yaml_reader import YamlConfigReader
from src.logger.logger_mixin import LoggerMixIn

ACCESSOR_BUILDER_MAP = {
    'yaml': lambda x: YamlConfigAccessor(path=x)
}
CONFIG_READER_MAP = {
    'yaml': YamlConfigReader()
}
FORMATTER_MAP = {
    'xls': lambda x: ToExcelFormatter(output_path=x)
}


class Processor(LoggerMixIn):
    def __init__(self, params: ProcessParams):
        builder = StructureBuilder(ACCESSOR_BUILDER_MAP[params.config_type])
        self.params = params
        self.structure = builder.build(params.config_structure)
        self.reader = ConfigDirectoryReader(params.read_path, CONFIG_READER_MAP[params.config_type])
        self.formatter = FORMATTER_MAP[params.use_format](params.output_path)

    def start(self):
        result: List[Dict] = []

        for config in self.reader.read_configs_files(self.params.file_pattern):

            for data in self.structure.capture(config):
                result.append(data)

        self.formatter.write_to_format(result)
