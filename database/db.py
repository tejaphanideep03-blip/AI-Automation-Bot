import sqlite3

from config.constants import DATABASE


def create_db():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sent_news(
            link TEXT PRIMARY KEY
        )
    """)

    conn.commit()

    conn.close()


def already_sent(link):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM sent_news WHERE link=?",
        (link,)
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None


def save_news(link):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        "INSERT OR IGNORE INTO sent_news VALUES(?)",
        (link,)
    )

    conn.commit()

    conn.close()