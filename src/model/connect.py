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

try:
    cur.execute("SELECT 1")
except psycopg2.OperationalError as e:
    print("Ошибка подключения к базе данных:", e)
else:
    print("Подключение к базе данных успешно")
