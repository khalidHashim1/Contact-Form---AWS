import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ContactFormSubmissions')
ses = boto3.client('ses', region_name='us-east-1')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        item = {
            'id': str(uuid.uuid4()),
            'name': body['name'],
            'email': body['email'],
            'message': body['message'],
            'submittedAt': datetime.utcnow().isoformat()
        }

        # Store in DynamoDB
        table.put_item(Item=item)

        # Send email
        ses.send_email(
            Source='khalidhashim1422@gmail.com',  # Verified SES email
            Destination={'ToAddresses': ['khalidhashim1422@gmail.com']},  # Your inbox
            Message={
                'Subject': {'Data': f"New Contact Form Submission from {body['name']}"},
                'Body': {
                    'Text': {
                        'Data': f"Name: {body['name']}\nEmail: {body['email']}\nMessage: {body['message']}"
                    }
                }
            }
        )

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'message': 'Form submitted successfully!'})
        }

    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'message': 'Error submitting form.'})
        }
