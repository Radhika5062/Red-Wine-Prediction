from mlProject import logger 
import pandas as pd
from mlProject.entity.config_entity import DataValidationConfig
import os

class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config = config 
    
    def validate_all_columns(self) -> bool: 
        try:
            validation_status = None 

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status} \n")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status} \n")
            
            return validation_status
        except Exception as e:
            raise e 
    
    def validate_all_data_type(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema

            for col in all_cols:
                for sch in all_schema:
                    # if (col == sch):
                    #     print(f"{all_schema[sch]}")
                    # else:
                    #     pass
                    if ((col == sch ) and (data.dtypes[col] == all_schema[sch])):
                        validation_status = True
                        with open(self.config.STATUS_FILE, 'w') as f:
                            f.write(f'Validation status from dtypes function: {validation_status}')
            
            return validation_status
        except Exception as e:
            raise e