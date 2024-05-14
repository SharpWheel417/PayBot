from src.model.connect import cur, conn


class Admins:
    def __init__(self):
        pass

    def insert(self, chat_id: str) -> str:
        'Берем сообщение из БД'
        max_id_query = "SELECT MAX(id) FROM admins"
        cur.execute(max_id_query)
        max_id = cur.fetchone()[0]

        # Increment the maximum id value by 1 to get the new id value
        new_id = max_id + 1

        query = f"INSERT INTO admins (id, chat_id) VALUES ({new_id}, '{chat_id}')"
        try:
            cur.execute(query)
            conn.commit()

        except Exception as e:
            conn.rollback()
            print("Error:", e)

    def delete(self, chat_id: str) -> bool:
        'Ставим сообщение из БД'
        query = f"DELETE FROM admins WHERE chat_id = '{chat_id}'"
        try:
            cur.execute(query)
            conn.commit()
            return True

        except Exception as e:
            conn.rollback()
            print("Error:", e)
            return False

    def select(self) -> bool:
        'Ставим сообщение из БД'
        query = f"SELECT * FROM admins"
        try:
            cur.execute(query)
            txt = cur.fetchall()
            return txt

        except Exception as e:
            conn.rollback()
            print("Error:", e)
            return "False"

    def add(self, chat_id: str):
        self.insert(chat_id)

    def remove(self, chat_id: str) -> bool:
        self.delete(chat_id)

    def get(self) -> bool:
        return self.select()


a = Admins()