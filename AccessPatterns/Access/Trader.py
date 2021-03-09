
"""
 Scripts with purpose to realize traders registers operations
"""

from dynamodb.DynamoDB import Dynamodb


class Trader:

    def __init__(self, table):

        self.client = Dynamodb().client_dynamo(table)

    def register_trader(self, cpf, name, lastname, email, birthdate, address, profile):
        """
        Function for register trader on platform

        :param cpf: cpf trader user
        :param name: name trader user
        :param lastname: last name trader user
        :param email: email trader user
        :param birthdate: birth date user
        :param address: address trader
        :param profile: investor profile
        """
        try:
            self.client.put_item(
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
        """
        Function of the traders registers update on platform

        :param cpf: cpf trader user
        :param field: field that will be updated
        :param value: new value
        """
        self.client.update_item(
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
        self.client.delete_item(
            Key={
                "PK": f"TRADER#{cpf}",
                "SK": f"#METADATA#{cpf}"
            }
        )
        print('Trader successfully deleted!')
