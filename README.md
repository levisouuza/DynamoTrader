# DynamoTrader


Com a finalidade de aprender mais sobre AWS, criei o projeto DynamoTrader, que consiste em utilizar DynamoDB, um serviço de banco de dados NoSQL totalmente gerenciado pela AWS, para simular uma repositório de investimentos que tem a função de persistir dados de cadastro e operações dos traders.

Como são transações em High Frenquency, escolhi o DynamoDB devido sua flexibilidade de Schema (Key-Value e Documentos), baixissíma latência(10MS) e replicação em 3 AZ's garantindo suporte a Disaster Recovery. 

### Overview - NoSQL Databases.

BancoS de dados NoSQL - Not Only SQL - são utilizados quando geralmente precisamos persistir dados semiestruturados ou não estruturados. Enquanto os RDBMS funcionam baseados nas propriedades ACID (Atomicity, Consistency, Isolation, Durability), os NoSQL's funcionam seguindo a propriedade BASE (Basically Availabe Soft state Eventually Consistent), desta maneira, é possível entregar seus principais valores: Escalabilidade, Replicação de dados, Schema free, Performance e processamento distribuído.


### Sobre o DynamoDB:

Alguns conceitos são primordiais quando trabalhamos com o DynamoDB:

**Tabela**: Objeto principal onde os dados serão persistidos.

**Atributo**: Coluna/Carasterística do dado que será armazenado no DynamoDB. Como o DynamoDB tem Schema flexível não é necessário criá-la no momento da concepção da tabela. 

**Primary Key**: Identificador único do dado persistido no DynamoDB. Quando criamos a tabela no DynamoDB é necessário informar o nome e tipo dessa chave. Pode apresentar datatypes do tipo: string, number ou binary. Uma Primary Key pode ser do tipo:

	- PARTITION KEY: Atributo único. Função de hash interno que determina em qual partição ou local físico será persistido o dado.
	- COMPOSITE KEY (PARTITION KEY + SORT KEY): Usado quando o dado pode ser repitido.

**Tipos de Consistência**:

   	- EVENTUAL CONSISTENT READS(DEFAULT)
   	- STRONGLY CONSISTENT READS: Consistência forte de leitura e retorna o resultado que reflete todas as escritas que tiveram sucesso antes da leitura

**Índices**: Os índices nos ajudam a consultar atributos da coluna que não são a PrimaryKey. O DynamoDB apresenta dois tipo de Índices:

	- LOCAL SECONDARY INDEX (Suporte de ambas consistências)
		* Criado no momento da criação da tabela.
		* Mesma partition key da tabela
		* Diferente da sort key.

	- GLOBAL SECONDARY INDEX(EVENTUAL CONSISTENT)
		* Pode ser criado a qualquer momento.
		* Pode usar uma partition key diferente da tabela.

**Capacity Units (CUs)**: Conforme documentação da [AWS](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html) detalha a capacidade de transferência de sua operação. Quando criamos uma tabela, precisamos estabelecer dois de tipos CUs: 

	- Read Capacity Units: Representa uma consistência forte de leitura por segundo. Quanto maior o item que você deseja ler, maior será a RCU consumida (e cobrada por isso).
	- Write Capacity Units: Representa uma escrita por segundo de um item de 1Kb. Quanto maior o item que você escrever, maior será a WCU solicitada (e cobrada por isso).


## PROJETO

Diferente de bancos de dados relacionais, onde o Kick-off é dado na fase de modelagem dos dados, no DynamoDB pensamos inicialmente em como iremos acessar os dados antes de modelar a tabela. Chamamos isso de **Padrões de Acesso**. Logo abaixo estão os padrões de acesso que utilizaremos para o projeto.

1. TRADER
	- Registrar trader
	- Atualizar trader
	- deletar trader
	- consultar trader

2. INVESTMENTS
	- Realizar investimentos

Agora que identificamos os padrões de acesso, podemos modelar nossos casos de uso, onde podemos observar logo abaixo.

![ERD_dynamo](https://github.com/levisouuza/DynamoTrader/blob/master/images/ERD_dynamoDB.png)

Existem dois processos principais, *Traders* e *Investments*. Para trabalharmos com DynamoDB precisamos "esquecer" a característica dos RDBMS de normalização de tabelas e joins. No DynamoDB, todos os casos de uso serão persisitidos em um único objeto.

Após entendermos como os dados serão armazenados, podemos [criar](https://github.com/levisouuza/DynamoTrader/blob/master/Definition/CreateTable.py).

### Padrões de Acesso




