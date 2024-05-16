# Step 8
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
        # If you want to add log to file then use fileHandler
        logging.FileHandler(log_filepath),
        # If you want to add log to console then add StreamHandler
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("mlProjectLogger")

# Step 8 complete