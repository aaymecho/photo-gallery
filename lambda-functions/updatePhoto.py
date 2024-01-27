import json
import boto3  
from boto3.dynamodb.conditions import Key, Attr

REGION="us-east-1"
dynamodb = boto3.resource('dynamodb',region_name=REGION)
table = dynamodb.Table('PhotoGallery')

def lambda_handler(event, context):
    try:
        photoID=event['params']['path']['id']
        title=event['body-json']['title']
        description=event['body-json']['description']
        tags=event['body-json']['tags']

        table.update_item(
        Item={                        
                "PhotoID": str(photoID),
                "CreationTime": int(photoID),
                "Title": title,
                "Description": description,
                "Tags": tags,
            }
        )
                    
        return {
            "statusCode": 200,
            "body": json.dumps(photoID)
        }
    except:
        return {
            "error": "Something went wrong!"
        }