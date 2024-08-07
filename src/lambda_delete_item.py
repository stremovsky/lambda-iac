import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('table1')

def lambda_handler(event, context):
    if 'queryStringParameters' not in event or event['queryStringParameters'] is None or 'id' not in event['queryStringParameters']:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'Request query id parameter is missing'})
        }
    item_id = event['queryStringParameters']['id']
    response = table.delete_item(Key={'id': item_id})
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Item deleted'})
    }
