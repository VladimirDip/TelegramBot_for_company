import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('TOKEN_OF_BOT'))

ip = os.getenv('ip')

admins = [
    692468783,
]
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
DATABASE = str(os.getenv('DATABASE'))

POSTGRESURI = f'postgresql+psycopg2://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'
