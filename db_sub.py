"""
Use Python 3 and the sqlite3 module.
Database requires 2 fields: an auto-increment primary integer field and a field with the data type “string.”
Read from fileList and determine only the files from the list which end with a “.txt” file extension.
Add those file names from the list ending with “.txt” file extension within your database.
Print the qualifying text files to the console.
Provide good comments.
"""


import sqlite3

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

def commit(stmt):
	conn = sqlite3.connect('db_sub.db')
	with conn:
		cur = conn.cursor()
		try:
			cur.execute(stmt)
			conn.commit()
		except:
			print(stmt + ' is not a valid query.')
	conn.close()

def fetchall(stmt):
	conn = sqlite3.connect('db_sub.db')
	with conn:
		cur = conn.cursor()
		try:
			cur.execute(stmt)
			result = cur.fetchall()
		except:
			result = stmt + ' is not a valid query.'
			print(result)
	conn.close()
	return result

commit("create table if not exists tbl_strings(id integer primary key autoincrement, col_string string)")

for file in fileList:
	if file.endswith('.txt'):
		commit("insert into tbl_strings('col_string') values('{}')".format(file))
		print("{} inserted into database.".format(file))

print("\nAll records in database:")
for record in fetchall("select * from tbl_strings"):
	print(record)