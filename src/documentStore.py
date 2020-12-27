import boto3
from botocore.exceptions import ClientError
import os

BUCKET_NAME = 'unshackle-docs'

class DocumentStore:
    def __init__(self, docs_dir, parsed_dir):
        self.docs_dir = docs_dir
        self.parsed_dir = parsed_dir

        self.s3 = boto3.client('s3')


    def download(self, dir, id):
        object_name = str(id) + '.txt'
        print('Downloading ' + object_name)
        try:
            self.s3.download_file(BUCKET_NAME, object_name, dir + '/' + str(id) + '.txt')
        except Exception as e:
            print("Exception!!")
            print(e)
            return 

    def upload(self, id):
        filename = self.parsed_dir + str(id) + '.txt'
        print('Uploading ' + filename)
        with open(filename, 'rb') as f:
            self.s3.upload_fileobj(f, BUCKET_NAME, filename)
            
    def is_stored(self, id):
        filename = self.parsed_dir + str(id) + '.txt'
        try:
            self.s3.head_object(Bucket=BUCKET_NAME, Key=filename)
        except ClientError as e:
            return int(e.response['Error']['Code']) != 404
        return True
    
