
from dynamodb.DynamoDB import Dynamodb
from datetime import datetime, timedelta


class Investments:

    def __init__(self, table):

        self.dynamo_resource = Dynamodb().resource_dynamo().Table(table)

    def register_invest(self, cpf, transaction, ticker, date, quantity, price, operation, broker, status):
        try:
            ConsultActionDatetime = datetime.now()
            self.dynamo_resource.put_item(
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
                    "DatExclusion": int((ConsultActionDatetime + timedelta(days=1)).timestamp())
                }
            )

        except Exception as e:
            print(f'Transaction not completed! Register error - {e}')
            exit()

    def cancel_invest(self, cpf, transaction):
        output = self.dynamo_resource.get_item(
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
            self.dynamo_resource.update_item(
                Key={
                    "PK": f"TRANSACTION#{transaction}",
                    "SK": f"TRADER#{cpf}",
                },
                UpdateExpression='Set Situation = :NewData',
                ExpressionAttributeValues={
                    ':NewData': "C"
                }
            )