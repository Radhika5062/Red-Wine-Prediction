from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directories
from mlProject.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig
from mlProject import logger


class ConfigurationManager:
    def __init__(
        self,
        # ALl of these paths are coming from the constants package that we have imported. So our code is able to understand what
        # CONFIG_FILE_PATH is when we are trying to reference it.
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH
    ):
        # Now we need to read these yaml files. So above we have imported the utils.common package where our read_yaml function is 
        # defined so we are going to use it. 
        logger.info(f"Config file path is {config_filepath}")
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        # Lastly in the config.yaml file we needed to create directories too so we are going to use the create_directories
        # function from the common package. Self.config because we have defined a variable above self.config which is reading the
        # config_filepath. So this means this will have all the methods and variables of the config_yaml file which is 
        # artifacts_root.
        create_directories([self.config.artifacts_root])
    
    # Below we have written DataIngestionConfig as return type as we have already defined this above. Now what this will do is
    # it will only return the items which we have mentioned above. 
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # now we have already created self.config above in the construtor. This is able to read everything that is present in
        # the config.yaml file. We now are using it to get the data.ingestion part. Just above, we used it to read the
        # artifacts_root part and create that directory. 
        config = self.config.data_ingestion

        # now we need to create the data_ingestion directory under the artifacts directory.
        # we are passing this as list as this is the format expected in our function defined in common
        create_directories([config.root_dir]) 

        # once this is done, we are returning everything in data_ingestion
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL=config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE = config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema
        )

        return data_validation_config
    
    def get_data_transformation_config(self)-> DataTransformationConfig:
        config = self.config.data_transformation
        
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path = config.data_path
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path = config.test_data_path,
            model_name=config.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column=schema.name
        )
        return model_trainer_config