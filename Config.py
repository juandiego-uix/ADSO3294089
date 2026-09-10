import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config:

    MYSQL_HOST      = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER      = os.getenv('MYSQL_USER', '')
    MYSQL_PASSWORD  = os.getenv('MYSQL_PASSWORD', '')
    MYSQL_DB        = os.getenv('MYSQL_DB', '')
    MYSQL_PORT      = int(os.getenv('MYSQL_PORT', 3306))
    MYSQL_CURSORCLASS = os.getenv('MYSQL_CURSORCLASS', 'Cursor')
    MYSQL_SSL_CA    = os.getenv('MYSQL_SSL_CA', os.path.join(BASE_DIR, 'ca.pem'))