from AccessPatterns.Access.Investments import Investments
from AccessPatterns.Access.Trader import Trader
from AccessPatterns.Queries.Query import Queries
from Definition.CreateTable import Create
from Definition.CreateIndex import CreateIndex
from datetime import datetime
from random import randint

# Creating table
create_table = Create()
create_table.create_table_db('trader-transaction', 'PK', 'SK', 1, 1, 'DatExclusion')

#teste
# Register Trader
"""
Trader('trader-transaction').register_trader('11122233344', 'Levi', 'Souza', 'levis@gmail.com', '1995-06-08',
                                             'Wall Street, 22', 'Agressive')
Trader('trader-transaction').register_trader('22233344455', 'Tom', 'Brady', 'tom@gmail.com', '1977-08-03', 'Boston, 145'
                                             , 'Agressive')
"""

# Investing
"""
Investments('trader-transaction').register_invest('22233344455', randint(1000, 2000), 'MCHI', datetime.now(), 1,
                                                  '85.19', 'b', 'xp', 'A')
Investments('trader-transaction').register_invest('11122233344', randint(1000, 2000), 'AAPL', datetime.now(), 40,
                                                  '121.49', 'b', 'AVENUE', 'E')
Investments('trader-transaction').register_invest('22233344455', randint(1000, 2000), 'AMZN', datetime.now(), 10,
                                                  '3000.21', 'b', 'AVENUE', 'A')
                                                  """
"""
# Cancel investments
Investments('trader-transaction').cancel_invest('22233344455', 1356)

# Creating Global Secondary Index
CreateIndex('trader-transaction').global_index('SK', 'SKIndex', 1, 1)
CreateIndex('trader-transaction').global_index('Ticker', 'TickerIndex', 1, 1)
CreateIndex('trader-transaction').global_index('Situation', 'SituationIndex', 1, 1)
CreateIndex('trader-transaction').global_index('OperationType', 'OperationTypeIndex', 1, 1)
CreateIndex('trader-transaction').global_index('TransactionDate', 'TransactionDateIndex', 1, 1)

# Querying register trader
Queries('trader-transaction').query('S', 'SK', '22233344455', 'SKIndex')
"""



