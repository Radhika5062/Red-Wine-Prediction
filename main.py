# If we have logging functionality defined in a separate logging module then the import statement will look something like
#from src.mlProject.logging import logger

# If our logging is defined in the __init__.py file of the mlProject folder then our input statement will look something like
from mlProject import logger

logger.info("This is our custom log!")