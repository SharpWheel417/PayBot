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
        query = f"INSERT INTO orders (id, ids, username, chat_id, sum, course, profit, marje, date, state, status, timechk) VALUES ({max_id()+1}, '{ids}','{user}', '{chatId}', {summ}, {course}, {profit}, {marje}, '{current_date}', '{state}', 'request', 'start')"
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

    def get_sum(self, ids):
        query = f"SELECT sum FROM orders WHERE ids = '{ids}'"
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

    def  get_active(self, chat_id: str):
        query = f"SELECT ids, date, sum, timechk FROM orders WHERE chat_id = '{chat_id}' AND status = 'active'"
        try:
            cur.execute(query)
            result = cur.fetchall()
            o = {
                'ids': result[0][0],
                'date': result[0][1],
                'sum': result[0][2],
                'timechk': result[0][3],
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
            print("Статус заказа изменен на: ", status)
            return True
        except Exception as e:
            conn.rollback()
            print("Error:", e)
            return False

    def set_time(self, ids: str) -> bool:
        'Обновляем state заказа'
        date = datetime.datetime.now()
        query = f"UPDATE orders SET date = '{date}' WHERE ids = '{ids}'"
        print(query)
        try:
            cur.execute(query)
            conn.commit()
            print("Время заказа изменен на: ", date)
            return True
        except Exception as e:
            conn.rollback()
            print("Error:", e)
            return False

    def where_status(self, status: str) -> bool:
        'Обновляем state заказа'
        query = f"SELECT ids FROM orders WHERE status = '{status}'"
        print(query)
        try:
            cur.execute(query)
            conn.commit()
            print("Статус заказа изменен на: ", status)
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


    def get_timechk(self):
        query = f"SELECT ids, date FROM orders WHERE timechk = 'start'"
        try:
            cur.execute(query)
            result = cur.fetchall()
            return result
        except Exception as e:
            conn.rollback()
            print("Error:", e)

    def set_timechk(self, timechk: str, ids: str) -> bool:
        query = f"UPDATE orders SET timechk = '{timechk}' WHERE ids='{ids}'"
        try:
            cur.execute(query)
            conn.commit()
            print("Время проверки изменено")
            return True
        except Exception as e:
            conn.rollback()
            print("Error:", e)
            return False


    def get_orders(self, status: str):
         ##TODO Хз какой статус поставить
        query = f"SELECT * FROM orders WHERE status = '{status}'"
        print(query)
        try:
            cur.execute(query)
            result = cur.fetchall()
            return result
        except Exception as e:
            conn.rollback()
            print("Error:", e)
            return []


    def get_sum(self, ids):
        query = f"SELECT sum FROM orders WHERE ids = '{ids}'"
        try:
            # Вставьте текущую дату в таблицу "order"
            cur.execute(query)
            result = cur.fetchall()
            return result[0][0]
        except Exception as e:
            conn.rollback()
            print("Error:", e)
            return "Error"

    ###
    ### Заказы в работе
    ###
    def in_work(self):
        'Получаем список заказов вработе'
        ##TODO Хз какой статус поставить
        return self.get_orders('active')

    ###
    ### Заказы в запросе
    ###
    def requests(self):
        'Получаем список заказов запросов'
        ##TODO Хз какой статус поставить
        return self.get_orders('request')

    ###
    ### Заказы выполненые
    ###
    def completes(self):
        'Получаем список выполненыех заказов'
        ##TODO Хз какой статус поставить
        return self.get_orders('complete')


    ###
    ### Заказы отмененные
    ###
    def cancles(self):
        'Получаем список отмененных заказов'
        ##TODO Хз какой статус поставить
        return self.get_orders('cancle')



order = Order()



def get_order_ids( chat_id: str) -> str:
    'Берем заказ из БД'

    query = f"SELECT ids FROM orders WHERE chat_id = '{chat_id}' AND state = 'query'"
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

def get_order_sum( chat_id: str) -> str:
    'Берем заказ из БД'

    query = f"SELECT sum FROM orders WHERE chat_id = '{chat_id}'"
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



def close_order(chat_id: str):
    'Обновляем заказ в БД'

    query = f"DELETE FROM orders WHERE chat_id = '{chat_id}' AND state='query' "
    print(query)
    try:
        cur.execute(query)
        conn.commit()  # Не забудьте подтвердить транзакцию, если требуется
        print("Заказ отменен")
    except Exception as e:
        conn.rollback()
        print("Error:", e)


def recipt_order(ids: str, status: str):
    'Обновляем заказ в БД'

    query = f"UPDATE orders SET state = 'request', status='{status}' WHERE chat_id = '{ids}', state = 'query'"
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