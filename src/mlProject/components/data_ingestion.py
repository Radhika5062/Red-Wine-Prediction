import os
# using the request data we will be able to download the data from url itself. 
import urllib.request as request
# with the help of zipfile package, we will be able to unzip the file. 
import zipfile
from mlProject import logger
# We are using this file to check the size of the file downloaded.
from mlProject.utils.common import get_size
from mlProject.entity.config_entity import DataIngestionConfig
from pathlib import Path

# defining data ingestion class
class DataIngestion:
    # first we will pass the DataIngestionConfig that we have received from the configuration manager to constructor.
    def __init__(self, config:DataIngestionConfig):
        self.config = config
     
    # now first we are downloading the file
    def download_file(self):
        #In the if function, we are saying that if the local_data_path 
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with the info \n {headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    # Now once the data is downloaded, we need to extract the zip file
    def extract_zip_file(self):
        """
            zip_file_path: str
            Extracts the zip file into data directory
            Function returns none
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)