    
from dynamodb.credentials import Access_Key_ID, Secret_Access_Key, Region
import boto3


class Dynamodb:

    def __init__(self):

        self.session = boto3.session.Session(aws_access_key_id=Access_Key_ID,
                                             aws_secret_access_key=Secret_Access_Key,
                                             region_name=Region)

        self.resource = self.session.resource(service_name='dynamodb')
        self.client = self.session.client(service_name='dynamodb')

    def client_dynamo(self):
        return self.client

    def resource_dynamo(self):
        return self.resource
