#Deletes all entries in the table.
import sqlite3


conn = sqlite3.connect('diary.db')

sql_query = """
DELETE from Diary 

"""
conn.execute(sql_query)
conn.commit()
conn.close()
