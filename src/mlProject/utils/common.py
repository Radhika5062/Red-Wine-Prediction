# Step 10
# In this file we write utility related functions
# Whenever we do end to end projects then we use some functions very frequently.
# We are using config.yaml and schema.yml
# When we read these yaml files then we need to use pyYaml package that we have added in the requirements.txt file.
# Whatever functions we use frequently in different components, instead of creating then in all the components where
# they will be used, we put them in the utils folder in a file called common.py. 
# some common functionalities that are used are - reading a YAML file, writing a YAML file, loading object which is loading
# our model, saving object which is saving our trained model. These are then created in common.py file. 

import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib 
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path 
from typing import Any

# ensure_annotations is a decorator
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
        reads yaml file and returns

        Args:
            path_to_yaml (str): path like input
        
        Raises:
            ValueError: if yaml file is empty
            e: empty file
        
        Returns:
            ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """
        create list of directories

        Args:
            path_to_directories(list): list of path of directories
            ignore_log(bool, optional): ignore if multiple dirs is to be created. 
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok = True)
        if verbose:
            logger.info(f"Created Directory at: {path}")

@ensure_annotations
def save_json(path:Path, data:dict):
    """
        Save json data
        
        Args:
            path(Path): path to json file
            data(dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent = 4)
    logger.info(f"Json file saved at: {path}")

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    """
        load json files

        Args:
            path(Path): path to json file
        
        Returns:
            ConfigBox: data as class attributes instead of dict
        
    """
    with open(path) as f:
        content = json.load()
    logger.info(f"Json file loaded successfully from {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any, path:Path):
    """
        Save binary file
        Args:
            data(Any): data to be saved as binary
            path(Path): path to binary file
    """
    joblib.dump(value=data, filename = path)
    logger.info(f"binary file saved at {path}")

@ensure_annotations
def load_bin(path:Path) -> Any:
    """
        load binary data
        Args:
            path(Path):path tp binary file
        
        Returns:
            Any: Object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from {path}")
    return data 

@ensure_annotations
def get_size(path:Path) -> str:
    """
        get size in KB

        Args:
            path(Path): path of the file
        
        Returns:
            str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

# Step 10 complete