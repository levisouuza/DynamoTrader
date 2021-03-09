
"""
    Script to instance client Dynamodb
"""

from dynamodb.credentials import Access_Key_ID, Secret_Access_Key, Region
import boto3


class Dynamodb:

    def __init__(self):

        self.session = boto3.session.Session(aws_access_key_id=Access_Key_ID,
                                             aws_secret_access_key=Secret_Access_Key,
                                             region_name=Region)

        self.resource = self.session.resource(service_name='dynamodb')
        self.client = self.session.client(service_name='dynamodb')

    def client_dynamo(self, table, ddl='N', index='N'):
        """
        Function to create client or resource to manipulate Dynamodb

        :param table: table name
        :param ddl: if ddl = 'S' means create table
        :param index: if index = 'S' means create index
        :return: client Dynamodb
        """
        if ddl == 'N' and index == 'N':

            client_table = self.resource.Table(table)

            try:
                client_table.creation_date_time

            except Exception as e:
                print(e)
                exit()

        elif ddl == 'S' and index == 'S':
            client_table = self.client

        else:
            client_table = self.resource

        return client_table

