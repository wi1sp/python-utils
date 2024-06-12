import os
import re
from collections.abc import Iterator
from pathlib import Path
from typing import Any, Optional

from configs_to_format.configs_reader.base_config_reader import BaseConfigReader
from logger.logger_mixin import LoggerMixIn


class ConfigDirectoryReader(LoggerMixIn):
    def __init__(self, configs_directory: Path, config_reader: BaseConfigReader):
        self.path = configs_directory
        self.config_reader = config_reader

    def read_configs_files(self, file_pattern: Optional[str] = None) -> Iterator[Any]:
        path = str(self.path)
        pattern = None if file_pattern is None else re.compile(file_pattern)

        for config in os.listdir(path):
            config_path = os.path.join(path, config)
            if not os.path.isdir(config_path):
                print(f"Skipped '{config_path}' due it not directory")
                continue

            for config_file in os.listdir(config_path):
                file_path = os.path.join(config_path, config_file)

                if not os.path.isfile(file_path) or (pattern is not None and not pattern.match(config_file)):
                    print(f"Skipped '{file_path}' due its not math config file format")
                    continue

                yield self.config_reader.read_from_path(file_path)
