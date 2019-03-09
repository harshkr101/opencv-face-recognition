import sqlite3

db="face"
conn=sqlite3.connect(db)
c=conn.cursor()
def enter_data(line):
    conn.execute(line)
    conn.commit()

conn.close()