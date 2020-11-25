import sqlite3


def db():

    database = 'database.db'
    conn = sqlite3.connect(database)
    c = conn.cursor()
    query = "INSERT INTO table (cvv, cnumber, cexp)  VALUES ('data1', 'data2', 'data3')"
    c.execute(query)
    conn.commit()
    conn.close()
    print('Added to DB')