from src.model.connect import cur, conn


class Stats():
  def __init__(self) -> None:
    pass

      ###Берех их бд по запросу
  def take(self, query: str):
    try:
      cur.execute(query)
      txt = cur.fetchall()
      if txt != "":
          return txt
    except Exception as e:
      conn.rollback()
      print("Error:", e)

  def all_users(self):
    'Получаем всех пользователей из БД'
    return self.take("SELECT * from users")

  def orders(self):
    return self.take("SELECT COUNT(*) from orders WHERE status='complete'")[0][0]

  def all_money(self):
    return self.take("SELECT SUM(CAST(profit AS NUMERIC)) FROM orders WHERE status = 'complete'")[0][0]

stats = Stats()