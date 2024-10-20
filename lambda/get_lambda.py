import json
import boto3
import os

sqs = boto3.client('sqs')
QUEUE_URL = os.environ['QUEUE_URL']

def handler(event, context):
    response = sqs.receive_message(
        QueueUrl=QUEUE_URL,
        MaxNumberOfMessages=1
    )
    
    messages = response.get('Messages', [])
    if messages:
        message = messages[0]
        sqs.delete_message(
            QueueUrl=QUEUE_URL,
            ReceiptHandle=message['ReceiptHandle']
        )
        return {
            'statusCode': 200,
            'body': message['Body']
            
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'No messages in the queue'})
        }
