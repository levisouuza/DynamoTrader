
"""
    Scripts to create Global Secondary Index Dynamodb table.
"""

from dynamodb.DynamoDB import Dynamodb


class CreateIndex:

    def __init__(self, table):

        self.table = table
        self.dynamo = Dynamodb().client_dynamo(table, 'S', 'S')

    def global_index(self, attribute, index_name, read, write):
        """
        Function to create global secondary index dynamodb.

        :param attribute: attribute name
        :param index_name: index name
        :param read: quantity capacity units read.
        :param write: quantity capacity units write.
        :return:
        """
        try:
            index = self.dynamo.update_table(
                TableName=f"{self.table}",
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
