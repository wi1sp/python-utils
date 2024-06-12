from dataclasses import dataclass
from typing import Optional

from configs_to_format.config_structure.config_field import ConfigField


@dataclass(frozen=True, eq=False)
class ProcessParams:
    config_structure: ConfigField
    file_pattern: Optional[str] = None
