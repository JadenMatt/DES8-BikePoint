# Import packages

import requests
import os
import json 
from datetime import datetime 
import logging 
import time

# API endpoint we want to extract data from

url = 'https://api.tfl.gov.uk/BikePoint/'

# Create folder for extracted data

data_dir = 'data'
os.makedirs(data_dir, exist_ok = True)

# Create a timestamp so each extract gets a unique filename

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S') # - Don't use / when creating a file name
filename = f'{data_dir}/{timestamp}.json' 


# Set up retry setting in case the API fails

max_retry = 5
attempt = 0
delay = 10

# While loop

while attempt < max_retry:

    # Send a GET request to the API

    response = requests.get(url)

    # Set status variable 

    status = response.status_code

    # If statement based on status code

    if 200<= status < 300:
        data = response.json() # Convert JSON into python variable

        if len(data)>0: # Incase API worked but no data recieved
            try:

                with open(filename, 'w') as file:
                    json.dump(data, file) # Open the output file and write the API data to it as JSON
                print(f'{filename} was successfully saved :)') # Print success message for user

            except Exception as e:
                print(f'An error has occured {e}')
            break

        else: 
            print('No data returned')
            break
    

    elif status < 200 or status >= 500: # elif statement for client side errors
        time.sleep(delay)
        attempt += 1
        print(f'Status_code: {status}. Retrying, attempt number {attempt}')

    else:
        print(f'Error, Status code {status}, Fix it') # Statement for all other erors
        break
