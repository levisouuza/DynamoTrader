
"""
    Scripts of create dynamodb table
"""

from dynamodb.DynamoDB import Dynamodb


class Create:
    def __init__(self):

        self.dynamo_client = Dynamodb().client_dynamo()
        self.dynamo_resource = Dynamodb().resource_dynamo()

    def create_table_db(self, table, pk_name, sk_name, read, write, ttl=None):

        try:
            """
            self.dynamo_client.create_table(
                TableName=f'{table}',
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
"""
            def update_ttl():
                self.dynamo_client.update_time_to_live(
                    TableName=f"{table}",
                    TimeToLiveSpecification={
                        "Enabled": True,
                        "AttributeName": f"{ttl}"
                    }
                )

            if ttl is None:
                pass
                print(ttl)
            else:
                try:
                    update_ttl()
                    print('TTL Criado')
                except Exception as e:
                    raise Exception("Erro ao criar TTL")

            print(f"Table {table} created successfully.")
            return True

        except Exception as e:
            print(f"Could not create table. Error:{e}")
