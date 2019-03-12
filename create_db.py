import sqlite3

conn = sqlite3.connect('diary.db')

sql_query = """
CREATE TABLE IF NOT EXISTS Diary (
  id INTEGER PRIMARY KEY,
  title TEXT,
  journalentry TEXT,
  journaldate TEXT UNIQUE
);
"""
conn.execute(sql_query)
conn.close()
