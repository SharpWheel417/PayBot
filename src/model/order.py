from src.model.connect import cur, conn
import datetime
import uuid


class Order:
    def __init__(self) -> None:
        pass
    
    
    def set(self, summ: float, course: float, profit: float, marje: float,  user: int, chatId: int, state: str) -> bool:
        'Заносим заказ в БД'

        current_date = datetime.datetime.now()
        ids = str(uuid.uuid4())
        query = f"INSERT INTO orders (id, ids, username, chat_id, sum, course, profit, marje, date, state, status) VALUES ({max_id()+1}, '{ids}','{user}', '{chatId}', {summ}, {course}, {profit}, {marje}, '{current_date}', '{state}', 'active')"
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

    def check(self, chat_id) -> bool:
        '''
            Проверка, существует ли незавершенный заказ у пользователя
        '''
        query = f"SELECT EXISTS(SELECT 1 FROM orders WHERE chat_id = '{chat_id}' AND status = 'active')"
        try:
            cur.execute(query)
            result = cur.fetchall()
            print(result[0][0])
            return result[0][0]
        except Exception as e:
            conn.rollback()
            print("Error:", e)
            return "Error"

    def get_active(self, chat_id: str):
        query = f"SELECT ids, date, sum FROM orders WHERE chat_id = '{chat_id}' AND status = 'active'"
        try:
            cur.execute(query)
            result = cur.fetchall()
            o = {
                'ids': result[0][0],
                'date': result[0][1],
                'sum': result[0][2],
                }
            return o
        except Exception as e:
            conn.rollback()
            print("Error:", e)
            return "Error"
        
        
    def state(self, state: str, ids: str) -> bool:
        'Обновляем state заказа'
        query = f"UPDATE orders SET state = '{state}' WHERE ids = '{ids}'"
        print(query)
        try:
            cur.execute(query)
            conn.commit()
            print("Квитанция принята")
            return True
        except Exception as e:
            conn.rollback()
            print("Error:", e)
            return False
        
    def status(self, status: str, ids: str) -> bool:
        'Обновляем state заказа'
        query = f"UPDATE orders SET status = '{status}' WHERE ids = '{ids}'"
        print(query)
        try:
            cur.execute(query)
            conn.commit()
            print("Квитанция принята")
            return True
        except Exception as e:
            conn.rollback()
            print("Error:", e)
            return False
        
    def email_url(self, email: str, url:set, chat_id: str) -> bool:
        'Обновляем email и url заказа'
        query = f"UPDATE orders SET email = '{email}', url = '{url}' WHERE chat_id = '{chat_id}' AND status = 'active'"
        print(query)
        try:
            cur.execute(query)
            conn.commit()
            print("email and url занесены в БД")
            return True
        except Exception as e:
            conn.rollback()
            print("Error:", e)
            return False
            
    def chat_id(self, ids: str):
        'Получаем chat_id заказа'
        query = f"SELECT chat_id FROM orders WHERE ids = '{ids}'"
        print(query)
        try:
            cur.execute(query)
            result = cur.fetchall()
            return result[0][0]
        except Exception as e:
            conn.rollback()
            print("Error:", e)
            



order = Order()



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
        if max_id < 1:
            return 0
        else:
            return max_id
    except Exception as e:
        conn.rollback()
        print("Error:", e)
        return 0