import json
import logging
import boto3
import dynamo

logger = logging.getLogger()
logger.setLevel(logging.INFO)
dynamodb = boto3.client('dynamodb')
table_name = 'adjacentSkills'

def get(event, context):
    logger.info(f'Incoming request is: {event}')
    # Set the default error response
    response = {
        "statusCode": 500,
        "body": "An error occured while getting post."
    }

    skills_id = event['pathParameters']['skillsId']

    skills_query = dynamodb.get_item(
        TableName=table_name, Key={'skillsid': {'S': skills_id}})

    if 'Item' in skills_query:
        adjskills = skills_query['Item']
        logger.info(f'Adjacent Skills are: {adjskills}')
        response = {
            "statusCode": 200,
            "body": json.dumps(dynamo.to_dict(adjskills))
        }

    return response
