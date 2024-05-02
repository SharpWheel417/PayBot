from connect import cur, conn


class Stats():
  def __init__(self) -> None:
    pass

      ###Берех их бд по запросу
  def take(self, query: str):
    try:
      cur.execute(query)
      txt = cur.fetchone()
      if txt != "":
          return txt
    except Exception as e:
      conn.rollback()
      print("Error:", e)


  def all_users(self):
    'Получаем всех пользователей из БД'
    return self.take("SELECT * from users")

  def orders(self):
    return self.take("SELECT * from order")

  def all_money(self):
    ##TODO У нас нет в БД поля с прибылью ???!!!!
    return self.take("SELECT all from orders WHERE status = 'complete'")