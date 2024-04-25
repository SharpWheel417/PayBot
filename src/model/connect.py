import psycopg2

### ПОДКЛЮЧЕНИЕ К БД
conn = None
cur = None

conn = psycopg2.connect(
host="localhost",
port=5432,
database="paybot",
user="admin",
password="admin")

cur = conn.cursor()