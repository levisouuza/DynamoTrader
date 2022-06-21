
from dynamodb.DynamoDB import Dynamodb


class Trader:

    def __init__(self, table):

        self.dynamo_resource = Dynamodb().resource_dynamo().Table(table)

    def register_trader(self, cpf, name, lastname, email, birthdate, address, profile):

        try:
            self.dynamo_resource.put_item(
                Item={
                    "PK": f"TRADER#{cpf}",
                    "SK": f"#METADATA#{cpf}",
                    "Name": name.capitalize(),
                    "LastName": lastname.capitalize(),
                    "Email": email,
                    "Birthdate": birthdate,
                    "Address": address,
                    "Profile": profile
                }
            )

        except Exception as e:
            print(f'Register error - {e}')
            exit()

    def update_trader(self, cpf, field, value):
        self.dynamo_resource.update_item(
            Key={
                "PK": f"TRADER#{cpf}",
                "SK": f"#METADATA#{cpf}"
            },
            UpdateExpression=f'Set {field} = :NewData',
            ExpressionAttributeValues={
                ':NewData': f"{value}"
            }
        )
        print('Register successfully updated!')

    def delete_trader(self, cpf):
        self.dynamo_resource.delete_item(
            Key={
                "PK": f"TRADER#{cpf}",
                "SK": f"#METADATA#{cpf}"
            }
        )
        print('Trader successfully deleted!')
