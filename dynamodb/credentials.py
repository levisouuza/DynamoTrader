
import platform

if platform.system() == 'Windows':
    directory = r'C:\Users\Levi\PycharmProjects\TraderTransaction\dynamodb\new_user_credentials.csv'
else:
    directory = '/home/ubuntu/TraderTransaction/dynamodb/new_user_credentials.csv'

credential_aws = open(directory, 'r').readlines()[1].split(',')

Access_Key_ID = credential_aws[2]
Secret_Access_Key = credential_aws[3]
Region = credential_aws[4]


