from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Dict


@dataclass(frozen=True, eq=False)
class ProcessParams:
    read_path: Path
    output_path: Path
    config_type: str
    use_format: str
    config_structure: Dict
    file_pattern: Optional[str] = None
