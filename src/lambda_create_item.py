import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('table1')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    if 'data' not in body:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'The request JSON has missing data parameter'})
        }
    item_id = body['id']
    item = {
        'id': item_id,
        'data': body['data']
    }
    table.put_item(Item=item)
    return {
        'statusCode': 200,
        'body': json.dumps({'id': item_id})
    }
