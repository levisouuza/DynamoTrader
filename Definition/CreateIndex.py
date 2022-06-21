
from dynamodb.DynamoDB import Dynamodb

class CreateIndex:

    def __init__(self):

        self.dynamo_client = Dynamodb().client_dynamo()

    def global_index(self, table, attribute, index_name, read, write):
        try:
            index = self.dynamo_client.update_table(
                TableName=f"{table}",
                AttributeDefinitions=[
                    {
                        "AttributeName": f'{attribute}',
                        "AttributeType": "S"
                    }
                ],
                GlobalSecondaryIndexUpdates=[
                    {
                        "Create": {
                            "IndexName": f'{index_name}',
                            "KeySchema": [
                                {
                                    "AttributeName": f"{attribute}",
                                    "KeyType": "HASH"
                                }
                            ],
                            "Projection": {
                                "ProjectionType": "ALL"
                            },
                            "ProvisionedThroughput": {
                                "ReadCapacityUnits": read,
                                "WriteCapacityUnits": write,
                            }

                        }
                    }
                ],
            )
            print(f"Secondary index - {index_name} - added!")
        except Exception as e:
            print(f"Error updating table: {e}")
