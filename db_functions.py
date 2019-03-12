import sqlite3


def execute_query(sql_query):
    """
    function to execute sql commands
    :return: returns values if select command used
    """
    # print(sql_query)
    with sqlite3.connect("diary.db") as con:
        cur = con.cursor()
        result = cur.execute(sql_query)
        con.commit()
    return result


def add_entry(text1,text2,date1):
    """
    function to add jounral entry title and text into the database
    :param text: text input by the user
    :return: None
    """
    sql_query = """insert into Diary(title, journalentry, journaldate) VALUES ( '%s','%s','%s' )""" % (text1, text2, date1)
    execute_query(sql_query)

def get_entries():
    """
    function to get all the entries from database
    :return:
    """
    sql_query = """select * from Diary """
    return execute_query(sql_query).fetchall()