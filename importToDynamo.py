# Python Script to insert csv records in dynamodb table.
from __future__ import print_function  # Python 2/3 compatibility
from __future__ import division  # Python 2/3 compatiblity for integer division

import boto3
#from boto3 import Table
from csv import reader
import time

# dynamodb and table initialization
#endpointUrl = "https://us-east-2.console.aws.amazon.com/dynamodbv2/home?region=us-east-2#service"
endpointUrl = "https://dynamodb.us-east-2.amazonaws.com"
dynamodb = boto3.resource('dynamodb', region_name='us-east-2', endpoint_url=endpointUrl)
tablename = 'adjacentSkills'
table = dynamodb.Table(tablename)
writeRate = 5
# write records to dynamo db
with open('./adjacentSkills.csv') as csv_file:
    tokens = reader(csv_file, delimiter=',')
    # read first line in file which contains dynamo db field names
    header = next(tokens)
    # read second line in file which contains dynamo db field data types
    headerFormat = next(tokens)
    # rest of file contain new records
    for token in tokens:
        print(token)
        item = {}
        for i, val in enumerate(token):
            print(val)
            key = header[i]
            item[key] = val
        print(item)
        table.put_item(Item=item)
        time.sleep(1)  # to accomodate max write provisioned capacity for table
