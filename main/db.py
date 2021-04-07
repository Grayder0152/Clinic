import sqlite3

DB_NAME = 'database.db'


def connect(func):
    def wrapper(**kwargs):
        db = sqlite3.connect(DB_NAME)
        try:
            cursor = db.cursor()
            return func(
                cursor,
                name=kwargs.get('name'),
                text=kwargs.get('text'),
                date=kwargs.get('date'),
                review_id=kwargs.get('review_id')
            )
        except sqlite3.OperationalError as e:
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
def select_reviews(cursor, *args, **kwargs) -> list:
    """
    Function can help you select all field from DB.

    Example: select_reviews() -> [(1, "Tom", "Tom`s text...", "28.03.2021")]

    :return:list with tuple
    """
    reviews = cursor.execute("SELECT * FROM Reviews").fetchall()
    return reviews


@connect
def delete_review(cursor, *args, **kwargs) -> None:
    """
    Function can help you delete one field from DB.

    :param review_id: int
    :return:None

    Example: delete_review(review_id=1) -> delete field with id=1
    Don`t forget to clear cookies!
    """
    cursor.execute("DELETE FROM Reviews WHERE id=?", (kwargs.get('review_id'),))


@connect
def insert_new_review(cursor, *args, **kwargs) -> None:
    """
    Function can help you create new field in DB.

    :param name: str
    :param text: str
    :param date: str
    :return:None

    Example: insert_new_review(name="Tom", text="Tom`s text...", date="28.03.2021") -> create new field
    """
    cursor.execute(
        "INSERT INTO Reviews(name, text, date) VALUES(?, ?, ?)",
        (
            kwargs.get('name'),
            kwargs.get('text'),
            kwargs.get('date')
        )
    )
