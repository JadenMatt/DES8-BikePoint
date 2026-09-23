# Import packages

import requests
import os
import json 
from datetime import datetime 
import logging 

# API endpoint we want to extract data from

url = 'https://api.tfl.gov.uk/BikePoint/'

# Create folder for extracted data

data_dir = 'data'
os.makedirs(data_dir, exist_ok = True)

# Create a timestamp so each extract gets a unique filename

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S') # - Don't use / when creating a file name
filename = f'{data_dir}/{timestamp}.json' 

# Send a GET request to the API

response = requests.get(url)

# If statement based on status code

status = response.status_code


# Convert JSON into python variable

data = response.json()

# Open the output file and write the API data to it as JSON

with open(filename, 'w') as file:
    json.dump(data, file)


