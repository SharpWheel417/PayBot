import datetime
from src.controller.sendmess import sendmess
from src.model.connect import cur, conn


class User():

    def __init__(self):
        pass

    def get_state(self, chat_id):
        'Получаем state пользователя'
        query = f"SELECT state FROM users WHERE chat_id = '{chat_id}'"
        print(query)
        try:
            cur.execute(query)
            result = cur.fetchall()
            return result[0][0]
        except Exception as e:
            conn.rollback()
            print("Ошибка получения state юзера:", e)
            # sendmess("Ошибка. Попробуйте выполнить команду /start")

    def state(self, state: str, chat_id: str) -> bool:
        '''
            Обновляем state пользователя
            Если поставить пустой username, то обновляем state по chat_id
        '''
        query = f"UPDATE users SET state = '{state}' WHERE chat_id = '{chat_id}'"
        print(query)
        try:
            cur.execute(query)
            conn.commit()
            print(" State usera обновлен")
            return True
        except Exception as e:
            conn.rollback()
            print("Ошибка обновления стейта юзера:", e)
            return False


user = User()


def add_new_user(chat_id, name, first_name) -> None:
    'Добавляем пользователя в бд нового пользователя'
    # Проверяем, существует ли пользователь с указанным chat_id
    print(f"Проверяем, существет ли пользователь {chat_id}")
    if name is None:
        name = "--"+first_name
    if first_name is None:
        name = '--unknown_user'
    try:
        cur.execute("SELECT id FROM users WHERE chat_id = '%s'", (chat_id,))
        existing_user = cur.fetchone()

        # Если пользователь существует, не выполняем вставку
        if existing_user:
            print("Пользователь с таким chat_id уже существует")
        else:
            current_date = datetime.datetime.now()
            query = f"INSERT INTO users (id, username, chat_id, full_name, date, state) VALUES ({max_id()+1}, '{name}', '{chat_id}', '{first_name}', '{current_date}', 'start')"
            # Вставляем пользователя, если он не существует
            cur.execute(query)
            conn.commit()  # Не забудьте подтвердить транзакцию, если требуется
            print("Новый пользователь добавлен")
    except Exception as e:
        conn.rollback()
        print("Error:", e)


def max_id():
    'Получаем максимальное id заказа'
    query = "SELECT MAX(id) FROM users"
    try:
        cur.execute(query)
        max_id = cur.fetchone()[0]
        if max_id is None:
            return 0
        return max_id
    except Exception as e:
        conn.rollback()
        print("Error:", e)
        return 0