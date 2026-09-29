import os
import logging
import boto3

logger = logging.getLogger(__name__)

def load_to_s3(data_dir:str  , AWS_ACCESS_KEY:str, AWS_BUCKET_NAME:str, AWS_SECRET_ACCESS_KEY:str):
    """ Uploads all files in the data directory to S3

    Args:
        data_dir (str): Where data is stored (locally)
        AWS_ACCESS_KEY (str): Linked to AWS IAM user
        AWS_BUCKET_NAME (str): S3 location where data is stored
        AWS_SECRET_ACCESS_KEY (str): Linked to AWS IAM user
    """


    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )


    files_to_upload = os.listdir(data_dir)

    for file in files_to_upload:
        file_to_upload = f'{data_dir}/{file}'

        try:
            s3_client.upload_file(file_to_upload, AWS_BUCKET_NAME, file)
            print(f'{file} uploaded successfully')
            logger.info(f'File: {file_to_upload} uploaded successfully')
            os.remove(file_to_upload)
        except Exception as e:
            print(f'An error has occured {e}')
            logger.error(f'An error has occured {e}')