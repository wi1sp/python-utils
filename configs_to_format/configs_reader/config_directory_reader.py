import os
import re
from collections.abc import Iterator
from pathlib import Path
from typing import Any, Optional

from configs_to_format.configs_reader.config_reader import ConfigReader


class ConfigDirectoryReader:
    def __init__(self, configs_directory: Path, config_reader: ConfigReader):
        self.path = configs_directory
        self.config_reader = config_reader

    def read_configs_files(self, file_pattern: Optional[str] = None) -> Iterator[Any]:
        path = str(self.path)
        pattern = None if file_pattern is None else re.compile(file_pattern)

        for config in os.listdir(path):
            config_path = os.path.join(path, config)
            if not os.path.isdir(config_path):
                continue

            for config_file in os.listdir(config_path):
                file_path = os.path.join(config_path, config_file)

                if not os.path.isfile(file_path) and (pattern is None or pattern.match(config_file)):
                    continue

                yield self.config_reader.read_from_path(file_path)
