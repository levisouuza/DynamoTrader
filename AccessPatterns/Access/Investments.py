
"""
 Script with purpose to realize registers and cancels investments transaction
"""

from dynamodb.DynamoDB import Dynamodb


class Investments:

    def __init__(self, table):

        self.client = Dynamodb().client_dynamo(table)

    def register_invest(self, cpf, transaction, ticker, date, quantity, price, operation, broker, status):
        """
        Function of register investment

        :param cpf: cpf trader user
        :param transaction: sequential transaction number
        :param ticker: acronym of the transaction asset
        :param date: date transaction(current date)
        :param quantity: investment vol asset
        :param price: current price transaction
        :param operation: type operation. B: Buy - S: Sell
        :param broker: Investment Platform
        :param status: Transaction status. A: In holding, C: Cancelled, E: Executed.
        """
        try:
            self.client.put_item(
                Item={
                    "PK": f"TRANSACTION#{transaction}",
                    "SK": f"TRADER#{cpf}",
                    "Ticker": ticker.upper(),
                    "TransactionDate": date.strftime('%Y-%m-%d %H:%M:%S'),
                    "Quantity": quantity,
                    "Price": price,
                    "OperationType": operation.upper(),
                    "Broker": broker.upper(),
                    "Situation": status.upper(),

                }
            )

        except Exception as e:
            print(f'Transaction not completed! Register error - {e}')
            exit()

    def cancel_invest(self, cpf, transaction):
        """
        Function to cancel investments in holding

        :param cpf: cpf trader user
        :param transaction: sequential transaction number
        """
        output = self.client.get_item(
            Key={
                "PK": f"TRANSACTION#{transaction}",
                "SK": f"TRADER#{cpf}",
            }
        )
        if output['Item']['Situation'] == 'E':
            print('Operation successfully executed. Unable to cancel')
        elif output['Item']['Situation'] == 'C':
            print('Unable to cancel. Operation Canceled!')
        else:
            self.client.update_item(
                Key={
                    "PK": f"TRANSACTION#{transaction}",
                    "SK": f"TRADER#{cpf}",
                },
                UpdateExpression='Set Situation = :NewData',
                ExpressionAttributeValues={
                    ':NewData': "C"
                }
            )