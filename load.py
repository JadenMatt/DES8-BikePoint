import os
import boto3
from dotenv import load_dotenv
import logging
from datetime import datetime

load_dotenv()

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME= os.getenv('AWS_BUCKET_NAME')

s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

log_dir ='log'
os.makedirs(log_dir, exist_ok = True)
log_filename = f'{log_dir}/load_{timestamp}.log'

# Configure logging so messages are written to the log file

logging.basicConfig(
    filename=log_filename,
    format= '%(asctime)s - %(levelname)s - %(message)s', 
    level= logging.INFO
)

# Create the logger and confirm it works

logger = logging.getLogger()
logger.info('Logger successfully Initiated')


files_to_upload = os.listdir('data')

for file in files_to_upload:
    file_to_upload = f'data/{file}'

    try:
        s3_client.upload_file(file_to_upload, AWS_BUCKET_NAME, file)
        print(f'{file} uploaded successfully')
        logger.info(f'File: {file_to_upload} uploaded successfully')
        os.remove(file_to_upload)
    except Exception as e:
        print(f'An error has occured {e}')
        logger.error(f'An error has occured {e}')