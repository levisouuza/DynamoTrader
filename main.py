from AccessPatterns.Access.Investments import Investments
from datetime import datetime
from random import randint

from dynamodb.DynamoDB import Dynamodb

dynamo_client = Dynamodb().client_dynamo()
dynamo_resource = Dynamodb().resource_dynamo().Table('trader-transaction')

Investments('trader-transaction').register_invest('22233344455', randint(1000, 2000), 'MCHI', datetime.now(), 1,
                                                  '85.19', 'b', 'xp', 'A')
Investments('trader-transaction').register_invest('11122233344', randint(1000, 2000), 'AAPL', datetime.now(), 40,
                                                  '121.49', 'b', 'AVENUE', 'E')
Investments('trader-transaction').register_invest('12387187126', randint(1000, 2000), 'AMZN', datetime.now(), 10,
                                                  '3000.21', 'b', 'AVENUE', 'A')





