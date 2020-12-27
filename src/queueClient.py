import boto3

QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/161051971148/docs'

class QueueClient:
    def __init__(self):
        self.sqs = boto3.client('sqs', region_name='us-east-1')

    def upload_new_doc(self, id):
        s3_url = 's3://unshackle-docs/parsed_texts/%s.txt' % (id)
        response = self.sqs.send_message(
            QueueUrl=QUEUE_URL,
            MessageAttributes={
                'document_url' : {
                    'DataType' : 'String',
                    'StringValue' : s3_url
                },
                'id' : {
                    'DataType' : 'String',
                    'StringValue' : str(id)
                }
            },
            MessageBody=('New doc')
        )

        