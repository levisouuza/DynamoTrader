
"""
    Scripts of create dynamodb table
"""

from dynamodb.DynamoDB import Dynamodb


class Create:

    def __init__(self, table):

        self.table = table
        self.dynamo = Dynamodb().client_dynamo(table, 'S')

    def create(self, pk_name, sk_name, read, write):
        """
        Function to create table on DynamoDB

        :param pk_name: primary key name or Partition key
        :param sk_name: secondary key name or classification key
        :param read: quantity capacity units read.
        :param write: quantity capacity units write.
        """
        try:
            self.dynamo.create_table(
                TableName=f'{self.table}',
                AttributeDefinitions=[
                    {
                        "AttributeName": f"{pk_name}",
                        "AttributeType": "S"
                    },
                    {
                        "AttributeName": f"{sk_name}",
                        "AttributeType": "S"
                    }
                ],
                KeySchema=[
                    {
                        "AttributeName": f"{pk_name}",
                        "KeyType": "HASH"
                    },
                    {
                        "AttributeName": f"{sk_name}",
                        "KeyType": "RANGE"
                    }

                ],
                ProvisionedThroughput={
                        "ReadCapacityUnits": read,
                        "WriteCapacityUnits": write
                    }

            )

            print(f"Table {self.table} created successfully.")

        except Exception as e:
            print(f"Could not create table. Error:{e}")





