import datetime
import os

from pathlib import Path
from typing import List, Dict

import pandas as pd

from .base_formatter import BaseFormatter


class ToExcelFormatter(BaseFormatter):
    def __init__(self, output_path: Path):
        self.output_path = output_path

    def write_to_format(self, records: List[Dict]):
        data = pd.DataFrame(records)

        path = os.path.join(
            str(self.output_path),
            f"{datetime.datetime.now().strftime('%Y-%m-%dT-%H-%M-%S-%f')}.xlsx"
        )

        data.to_excel(path)
