import boto3
import os

BUCKET_NAME = 'unshackle-docs'

# Schema makes things efficient
# Clean all docs before upload to 'docs'
# title - str
# tf-idfs per word?
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

    def upload(self, dir):
        print(dir)
        for filename in os.listdir(dir):
            print('Uploading ' + filename)
            self.s3.Object(BUCKET_NAME, filename).put(Body=open(dir + filename, 'rb'))

    
