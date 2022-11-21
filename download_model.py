import boto3
import pathlib
import os
from dotenv import load_dotenv
load_dotenv()

s_data = 'chest_model/chest.h5'
local_dist_file = 'healthcare/models/chest/'
dest_path = pathlib.Path(local_dist_file).resolve()




session = boto3.session.Session()
bucket_name = os.environ.get('BUCKET_NAME')
region =os.environ.get('REGION')
client = session.client('s3', region_name=region,aws_access_key_id=os.environ.get('ACCESS_KEY'),
                      aws_secret_access_key=os.environ.get('SECRET_KEY'))
fname = pathlib.Path(s_data).name

dl_path = dest_path /fname

client.download_file(bucket_name, s_data, str(dl_path))
