import sqlite3

conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("create table if not exists tbl_persons( \
        id integer primary key autoincrement, \
        col_fname text, \
        col_lname text, \
        col_email text \
    )")
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("insert into tbl_persons(col_fname, col_lname, col_email) values(?, ?, ?)", \
        ('Bob', 'Smith', 'bsmith@gmail.com'))
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("select col_fname, col_lname, col_email from tbl_persons")
    varPerson = cur.fetchall()
    for record in varPerson:
        msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(record[0], record[1], record[2])
        print(msg)
conn.close()