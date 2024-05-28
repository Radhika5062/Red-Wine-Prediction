from dataclasses import dataclass
from pathlib import Path

# In the code below, we are definfing the datatype of all the key value pairs in the config.yaml file for data_ingestion. 
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str 
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path 
    all_schema: dict 

@dataclass(frozen = True)
class DataTransformationConfig:
    root_dir: Path 
    data_path: Path 
    
@dataclass(frozen = True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path 
    test_data_path: Path 
    model_name: str 
    alpha: float 
    l1_ratio: float 
    target_column: str 