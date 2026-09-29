from Modules.log_initialiser import setup_log
from datetime import datetime
from Modules.extract_initialiser import extractor

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S') 

logger = setup_log('log', timestamp)
logger.info('Logger successfully Initiated')


# API endpoint we want to extract data from

url = 'https://api.tfl.gov.uk/BikePoint/'

# Create folder for extracted data

data_dir = 'data'

# Set up retry setting in case the API fails

max_retry = 5
delay = 10

extractor(url, data_dir, timestamp, max_retry, delay)