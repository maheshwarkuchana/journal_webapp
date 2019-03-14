import sqlite3


def create_db():

    conn = sqlite3.connect('diary.db')

    # Creating the table Diary

    sql_query = """
    CREATE TABLE IF NOT EXISTS Diary (
      id INTEGER PRIMARY KEY,
      title TEXT,
      journalentry TEXT,
      journaldate TEXT UNIQUE
    );
    """
    conn.execute(sql_query)


    conn.commit()
    conn.close()

