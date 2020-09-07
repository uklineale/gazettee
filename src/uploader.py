import boto3
import os

class Uploader:
    def __init__(self, pdf_dir, image_dir, parsed_dir, retitled_dir):
        self.pdf_dir = pdf_dir
        self.image_dir = image_dir
        self.parsed_dir = parsed_dir
        self.retitled_dir = retitled_dir

        self.s3 = boto3.resource('s3')

    def upload(self, dir):
        for filename in os.listdir(dir):
            src = self.retitled_dir + filename
            print('Uploading ' + src)
            self.s3.Object('unshackle-docs', src).put(Body=open(src, 'rb'))

    def upload_retitled(self):
        self.upload(self.retitled_dir)