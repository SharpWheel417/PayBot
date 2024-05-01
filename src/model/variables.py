from src.model.connect import cur, conn


class Vars:
    def __init__(self):
        pass

    def get_vars(self, type: str) -> str:
        'Берем сообщение из БД'
        query = f"SELECT text FROM vars WHERE type = '{type}'"
        try:
            cur.execute(query)
            txt = cur.fetchone()
            if txt is not None:
                return txt[0]
            else:
                return "Значение отсутствует"

        except Exception as e:
            conn.rollback()
            print("Error:", e)

    def set_vars(self, variables: float, type: str) -> bool:
        'Ставим сообщение из БД'
        query = f"UPDATE vars SET text = '{variables}' WHERE type = '{type}'"
        try:
            cur.execute(query)
            conn.commit()
            return True

        except Exception as e:
            conn.rollback()
            print("Error:", e)
            return False

    def phone(self):
        return self.get_vars('phone')

    def trade_type(self):
        return self.get_vars('trade_type')

    def usd(self):
        return self.get_vars('course_usd')

    def set_usd(self, usd:float) -> bool:
        if self.set_vars(usd, 'course_usd'):
            return True

    def marje(self):
        return self.get_vars('marje')


v = Vars()