from src.model.connect import cur, conn
import datetime
import uuid


def order(summ: int, type: str, userId: int, chatId: int, state: str):
    'Заносим заказ в БД'

    current_date = datetime.datetime.now()
    orderCode = str(uuid.uuid4())
    query = f"INSERT INTO orders (order_code, username, chat_id, money_type, sum, date_order, state) VALUES ('{orderCode}','{userId}', '{chatId}', '{type}', {summ}, '{current_date}', '{state}' )"
    print(query)
    try:
        # Вставьте текущую дату в таблицу "order"
        cur.execute(query)
        conn.commit()  # Не забудьте подтвердить транзакцию, если требуется
        print("Заказ создан")
    except Exception as e:
        conn.rollback()
        print("Error:", e)


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
