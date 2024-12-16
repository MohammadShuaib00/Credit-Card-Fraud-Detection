# creditfraud/entity/artifact_entity.py

import os
import sys
from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    raw_data_file_path: str
    train_file_path: str
    test_file_path: str
