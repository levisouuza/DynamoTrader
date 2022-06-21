
from boto3.dynamodb.conditions import Key
from dynamodb.DynamoDB import Dynamodb
from pprint import pprint
import time


class Queries:

    def __init__(self, table):

        self.dynamo_resource = Dynamodb().resource_dynamo().Table(table)

    def query(self, filter_index, key, value, index=''):
        if filter_index == 'S':
            while True:
                if not self.dynamo_resource.global_secondary_indexes or self.dynamo_resource.global_secondary_indexes[0]['IndexStatus'] != 'ACTIVE':
                    print('Waiting for index to backfill...')
                    time.sleep(5)
                    self.dynamo_resource.reload()
                else:
                    break

            if key == 'SK':
                qry = self.dynamo_resource.query(
                    IndexName=f'{index}',
                    KeyConditionExpression=Key(f'{key}').eq(f'TRADER#{value}'),
                )
            else:
                qry = self.dynamo_resource.query(
                    IndexName=f'{index}',
                    KeyConditionExpression=Key(f'{key}').eq(f'{value}'),
                )
        else:
            qry = self.dynamo_resource.query(
                KeyConditionExpression=Key(f'{key}').eq(f'TRADER#{value}'),
            )
        pprint([item for item in qry['Items']])