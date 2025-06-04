import logging
from datetime import datetime
import os
"""
Logger file is used to log the events that are happening during execution.

the logger file will save the logs into logs directory.

logger can log the following events
    
    - Exceptions
    - training Pipeline
    - testing Pipeline

"""

# Name of the log file
LOG_FILE = f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log" 
log_path = os.path.join(os.getcwd(),'logs')
os.makedirs(log_path,exist_ok=True)


LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)


logging.basicConfig(

    filename= LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)


logger = logging.getLogger(__name__)

