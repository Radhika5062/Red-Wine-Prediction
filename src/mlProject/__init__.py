# Step 9
# Instead of creating a separate logging module, we can also use this constructor file to add the same logging 
# functionality that we have added in the logging folder constructor

import os 
import sys
import logging 

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"

log_filepath = os.path.join(log_dir, "running_log")
os.makedirs(log_dir, exist_ok = True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("mlProjectLogger")

#Step 9 completed