import os
from datetime import datetime
import logging
import requests
import json
import time

logger = logging.getLogger(__name__)


def extractor(url:str, data_dir:str, timestamp:str, max_retry:int, delay:int):
    """Extracts JSON from specified URL and saves locally in the data dir

    Args:
        url (str): The URL you want to download JSON from
        data_dir (str): Where to save the data
        timestamp (str): The filename will be this
        max_retry (int): The max number of times API will be retried
        delay (int): How long to wait between retries (seconds)
    """

    # Create a timestamp so each extract gets a unique filename

    os.makedirs(data_dir, exist_ok = True)

    filename = f'{data_dir}/{timestamp}.json' 

    # Set up retry setting in case the API fails

    attempt = 0

    # While loop

    while attempt < max_retry:

        # Some variables need to be inside while loop as they need to change on each attempt

        response = requests.get(url) # Send a GET request to the API
        status = response.status_code  # Set status variable 

        # If statement based on status code

        if 200<= status < 300:
            data = response.json() # Convert JSON into python variable

            if len(data)>0: # Incase API worked but no data recieved
                try:

                    with open(filename, 'w') as file:
                        json.dump(data, file) # Open the output file and write the API data to it as JSON
                    print(f'{filename} was successfully saved :)') # Print success message for user
                    logger.info(f'File {filename} was successfully saved')

                except Exception as e:
                    print(f'An error has occured {e}')
                    logger.error(f'An error has occured {e}')
                break

            else: 
                print('No data returned')
                logger.warning('No data returned')
                break
        

        elif status < 200 or status >= 500: # elif statement for client side errors
            time.sleep(delay)
            attempt += 1
            print(f'Status_code: {status}. Retrying, attempt number {attempt}')
            logger.info()

        else:
            print(f'Error, Status code {status}, Fix it') # Statement for all other erors
            break
