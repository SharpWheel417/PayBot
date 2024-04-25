from src.model.connect import cur, conn

def mess(type: str):
    'Берем сообщение из БД'
    query = f"SELECT text FROM data WHERE type = '{type}'"
    try:
        cur.execute(query)
        txt = cur.fetchone()
        if txt != "":
            return txt[0]
        
    except Exception as e:
        conn.rollback()
        print("Error:", e)
