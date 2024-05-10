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

    def set_phone(self, phone:str) -> bool:
        if self.set_vars(phone, 'phone'):
            return True

    def trade_type(self):
        return self.get_vars('trade_type')

    def set_trade(self, trade:str) -> bool:
        if self.set_vars(trade, 'trade_type'):
            return True

    def usd(self):
        return self.get_vars('course_usd')

    def set_usd(self, usd:float) -> bool:
        if self.set_vars(usd, 'course_usd'):
            return True

    def marje(self):
        return self.get_vars('marje')

    def set_marje(self, marje:float) -> bool:
        if self.set_vars(marje, 'marje'):
            return True


v = Vars()