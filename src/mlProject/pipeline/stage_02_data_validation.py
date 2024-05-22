from mlProject import logger
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation

STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_columns()
        data_validation.validate_all_data_type()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e