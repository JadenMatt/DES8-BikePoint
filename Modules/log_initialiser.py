import os
import logging

def setup_log(log_dir:str, timestamp:str):
    """This function will initialise the logger.

    Args:
        dir_name (str): Where you want your logs saved
        timestamp (str): Timestamp will be the name of the log file
    """
    # Create a timestamp so each extract gets a unique filename

    #Create a folder for log files if it doesn't already exist

    log_dir ='log'
    os.makedirs(log_dir, exist_ok = True)
    log_filename = f'{log_dir}/{timestamp}.log'

    # Configure logging so messages are written to the log file

    logging.basicConfig(
        filename=log_filename,
        format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
        level= logging.INFO
    )

    # Create the logger and confirm it works

    return logging.getLogger()
    logger.info('Logger successfully Initialised')