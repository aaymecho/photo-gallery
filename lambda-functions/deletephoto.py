import json
import boto3
import time
import datetime


REGION="us-east-1"
dynamodb = boto3.resource('dynamodb',region_name=REGION)
table = dynamodb.Table('PhotoGallery')

def lambda_handler(event, context):
    photoID = event['params']['path']['id']
    try:
        table.delete_item(
            Key={
                "PhotoID" : str(photoID), 
                "CreationTime": int(photoID)
            }
        )
        return {
            "statusCode": 200,
            "photo_id": photoID
            
        }
    except:
        return {
            "photo_id": photoID,
            "msg": "Something went wrong",
        }