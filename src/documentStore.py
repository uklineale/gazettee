import boto3
import os

BUCKET_NAME = 'unshackle-docs'

# Schema makes things efficient
# Clean all docs before upload to 'docs'
# title - str
# tf-idfs per word?
class DocumentStore:
    def __init__(self, docs_dir, retitled_dir):
        self.pdf_dir = pdf_dir
        self.docs_dir = docs_dir
        self.retitled_dir = retitled_dir

        self.s3 = boto3.resource('s3')

    def get_documents(self, id):
        self.download(self.docs_dir)

    def download(self, dir, id):
        object_name = dir + '/' + str(id)
        # with
        # self.s3.download_file(BUCKET_NAME, object_name, )

    def upload(self, dir):
        for filename in os.listdir(dir):
            src = self.retitled_dir + filename
            print('Uploading ' + src)
            self.s3.Object(BUCKET_NAME, src).put(Body=open(src, 'rb'))

    def upload_retitled(self):
        self.upload(self.retitled_dir)

    
