import sqlite3

DB_NAME = '../database.db'


def connect(func):
    def wrapper(**kwargs):
        try:
            db = sqlite3.connect(DB_NAME)
            cursor = db.cursor()
            return func(
                cursor,
                name=kwargs.get('name'),
                text=kwargs.get('text'),
                date=kwargs.get('date'),
                review_id=kwargs.get('review_id')
            )
        except sqlite3.OperationalError as e:
            print(e)
            db.execute(
                'CREATE TABLE IF NOT EXISTS Reviews('
                'id INTEGER PRIMARY KEY autoincrement,'
                'name TEXT NOT NULL,'
                'text TEXT NOT NULL,'
                'date TEXT)'
            )
        finally:
            db.commit()
            db.close()

    return wrapper


@connect
def select_reviews(cursor, *args, **kwargs):
    reviews = cursor.execute("SELECT * FROM Reviews").fetchall()
    return reviews


@connect
def delete_review(cursor, *args, **kwargs):
    cursor.execute("DELETE FROM Reviews WHERE id=?", (kwargs.get('review_id'),))


@connect
def insert_new_review(cursor, *args, **kwargs):
    cursor.execute(
        "INSERT INTO Reviews(name, text, date) VALUES(?, ?, ?)",
        (
            kwargs.get('name'),
            kwargs.get('text'),
            kwargs.get('date')
        )
    )
