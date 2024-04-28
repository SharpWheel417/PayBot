from src.model.connect import cur, conn
import datetime
import uuid


class Order:
    def __init__(self) -> None:
        pass

    def get_state(self, username):
        query = f"SELECT state FROM orders WHERE username = '{username}'"
        try:
            # Вставьте текущую дату в таблицу "order"
            cur.execute(query)
            result = cur.fetchall()
            return result[0][0]
        except Exception as e:
            conn.rollback()
            print("Error:", e)
            return "Error"

    def check_order(self, username) -> bool:
        '''
            Проверка, существует ли незавершенный заказ у пользователя
        '''
        query = f"SELECT EXISTS(SELECT 1 FROM orders WHERE username = '{username}')"
        try:
            cur.execute(query)
            result = cur.fetchall()
            print(result[0][0])
            return result[0][0]
        except Exception as e:
            conn.rollback()
            print("Error:", e)
            return "Error"

    def get_active_order(self, username):
        query = f"SELECT ids, date FROM orders WHERE username = '{username}' AND state != 'cancel'"
        try:
            cur.execute(query)
            result = cur.fetchall()
            o = {
                'ids': result[0][0],
                'date': result[0][1],
                }
            return o
        except Exception as e:
            conn.rollback()
            print("Error:", e)
            return "Error"



order = Order()



def set_order(summ: int, user: int, chatId: int, state: str) -> bool:
    'Заносим заказ в БД'


    current_date = datetime.datetime.now()
    ids = str(uuid.uuid4())
    query = f"INSERT INTO orders (id, ids, username, chat_id, sum, date, state) VALUES ({max_id()+1}, '{ids}','{user}', '{chatId}', {summ}, '{current_date}', '{state}' )"
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

def get_order_ids( username: str) -> str:
    'Берем заказ из БД'

    query = f"SELECT ids FROM orders WHERE username = '{username}'"
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

def get_order_state( username: str) -> str:
    'Берем заказ из БД'

    query = f"SELECT state FROM orders WHERE username = '{username}'"
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


def recipt_order(username: str):
    'Обновляем заказ в БД'

    query = f"UPDATE orders SET state = 'receipt' WHERE username = '{username}'"
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