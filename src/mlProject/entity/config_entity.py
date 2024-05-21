from dataclasses import dataclass
from pathlib import Path

# In the code below, we are definfing the datatype of all the key value pairs in the config.yaml file for data_ingestion. 
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str 
    local_data_file: Path
    unzip_dir: Path