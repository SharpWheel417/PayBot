from src.model.connect import cur, conn
import datetime
import uuid


def order(summ: int, type: str, userId: int, chatId: int, state: str) -> bool:
    'Заносим заказ в БД'

    current_date = datetime.datetime.now()
    orderCode = str(uuid.uuid4())
    query = f"INSERT INTO orders (id, order_code, username, chat_id, money_type, sum, date_order, state) VALUES ({max_id()+1}, '{orderCode}','{userId}', '{chatId}', '{type}', {summ}, '{current_date}', '{state}' )"
    print(query)
    try:
        # Вставьте текущую дату в таблицу "order"
        cur.execute(query)
        conn.commit()  # Не забудьте подтвердить транзакцию, если требуется
        print("Заказ создан")
        return True
    except Exception as e:
        conn.rollback()
        print("Error:", e)
        return False

def get_order_code( username: str) -> str:
    'Берем заказ из БД'

    query = f"SELECT order_code FROM orders WHERE username = '{username}'"
    print(query)
    try:
        # Вставьте текущую дату в таблицу "order"
        cur.execute(query)
        result = cur.fetchall()
        return result[0][0]
    except Exception as e:
        conn.rollback()
        print("Error:", e)
        return "Error"

def get_order_sum( username: str) -> str:
    'Берем заказ из БД'

    query = f"SELECT sum FROM orders WHERE username = '{username}'"
    print(query)
    try:
        # Вставьте текущую дату в таблицу "order"
        cur.execute(query)
        result = cur.fetchall()
        return result[0][0]
    except Exception as e:
        conn.rollback()
        print("Error:", e)
        return "Error"


def update_order(username: str, link:str, email:str):
    'Обновляем заказ в БД'

    query = f"UPDATE orders SET link = '{link}', email = '{email}' WHERE username = '{username}'"
    print(query)
    try:
        cur.execute(query)
        conn.commit()  # Не забудьте подтвердить транзакцию, если требуется
        print("Заказ обновлен")
    except Exception as e:
        conn.rollback()
        print("Error:", e)


def close_order(username: str):
    'Обновляем заказ в БД'

    query = f"UPDATE orders SET state = 'cancel' WHERE username = '{username}'"
    print(query)
    try:
        cur.execute(query)
        conn.commit()  # Не забудьте подтвердить транзакцию, если требуется
        print("Заказ отменен")
    except Exception as e:
        conn.rollback()
        print("Error:", e)


def yes_order(username: str):
    'Обновляем заказ в БД'

    query = f"UPDATE orders SET state = 'yes' WHERE username = '{username}'"
    print(query)
    try:
        cur.execute(query)
        conn.commit()  # Не забудьте подтвердить транзакцию, если требуется
        print("Заказ отменен")
    except Exception as e:
        conn.rollback()
        print("Error:", e)




def max_id():
    'Получаем максимальное id заказа'
    query = "SELECT MAX(id) FROM orders"
    try:
        cur.execute(query)
        max_id = cur.fetchone()[0]
        return max_id
    except Exception as e:
        conn.rollback()
        print("Error:", e)