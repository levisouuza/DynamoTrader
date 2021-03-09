"""
    Scripts with purpose to query data of the table.
"""

from boto3.dynamodb.conditions import Key
from dynamodb.DynamoDB import Dynamodb
from pprint import pprint
import time


class Queries:

    def __init__(self, table):

        self.client = Dynamodb().client_dynamo(table)

    def query(self, filter_index, key, value, index=''):
        """
        Function to query data. Checks if the query will be carried out by index or key

        :param filter_index: S: Query by index - N: Query by key
        :param key: key name
        :param value: sought value
        :param index: index name
        :return: requested items
        """
        if filter_index == 'S':
            while True:
                if not self.client.global_secondary_indexes or self.client.global_secondary_indexes[0]['IndexStatus'] != 'ACTIVE':
                    print('Waiting for index to backfill...')
                    time.sleep(5)
                    self.client.reload()
                else:
                    break

            if key == 'SK':
                qry = self.client.query(
                    IndexName=f'{index}',
                    KeyConditionExpression=Key(f'{key}').eq(f'TRADER#{value}'),
                )
            else:
                qry = self.client.query(
                    IndexName=f'{index}',
                    KeyConditionExpression=Key(f'{key}').eq(f'{value}'),
                )
        else:
            qry = self.client.query(
                KeyConditionExpression=Key(f'{key}').eq(f'TRADER#{value}'),
            )
        pprint([item for item in qry['Items']])