from dataclasses import dataclass
from typing import Optional, List

from configs_to_format.config_structure.config_field import ConfigField


@dataclass(frozen=True, eq=False)
class ProcessParams:
    config_structure: List[ConfigField]
    file_pattern: Optional[str] = None
