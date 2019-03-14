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
    :param text1: title, text2: Journal entry input by the user date1: date when the entry was made
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

def edit_entry(text1,text2,id):

    """
    function to edit the diary entry and title
    :param id: id of the diary entry
    :return: None
    """
    sql_query = """UPDATE Diary set title= '%s', journalentry='%s' where id=%s""" % (text1, text2, id)
    execute_query(sql_query)
    return execute_query(sql_query).fetchall()


def fetch_entry(id):

    """
    function to edit the diary entry and title
    :param id: id of the diary entry
    :return: None
    """
    sql_query = """select * from Diary where id= %s""" % (id)
    execute_query(sql_query)
    return execute_query(sql_query).fetchall()

def search_entry(date1):
    """
       function to search the diary using date
       :param date1: date of the diary entry
       :return: None
       """

    sql_query = """select * from Diary where journaldate= '%s'""" % (date1)
    execute_query(sql_query)
    return execute_query(sql_query).fetchall()