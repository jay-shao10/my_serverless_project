import json
import boto3
import os

sqs = boto3.client('sqs')
QUEUE_URL = os.environ['QUEUE_URL']

def handler(event, context):
    body = json.loads(event['body'])
    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(body)
    )
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Message sent to SQS'})
    }