# If we have logging functionality defined in a separate logging module then the import statement will look something like
#from src.mlProject.logging import logger

# If our logging is defined in the __init__.py file of the mlProject folder then our input statement will look something like

from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e