from src.model.connect import cur, conn

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
            # Вставляем пользователя, если он не существует
            cur.execute("INSERT INTO users (username, chat_id, full_name) VALUES (%s, '%s', %s)", (name, chat_id, first_name))
            conn.commit()  # Не забудьте подтвердить транзакцию, если требуется
            print("Новый пользователь добавлен")
    except Exception as e:
        conn.rollback()
        print("Error:", e)
