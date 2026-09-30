from Modules.log_initialiser import setup_log
from datetime import datetime
from Modules.extract_initialiser import extractor
from dotenv import load_dotenv
import os
from Modules.load_initialiser import load_to_s3

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

load_dotenv()

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME= os.getenv('AWS_BUCKET_NAME')

load_to_s3(data_dir, AWS_ACCESS_KEY, AWS_BUCKET_NAME, AWS_SECRET_ACCESS_KEY)