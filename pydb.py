import sqlite3

if __name__ != "__main__":
	quit()

with sqlite3.connect(':memory:') as conn:
	cur = conn.cursor()

	#1) Create a database table in RAM named Roster that includes the fields ‘Name’, ‘Species’ and ‘IQ.’
	stmt = "create table if not exists tbl_roster (col_id integer not null primary key autoincrement, col_name string not null, col_species string not null, col_iq integer)"
	cur.execute(stmt)
	conn.commit()

	#2) Populate your new table with the following values:
	values = (
		("Jean-Baptiste Zorg", "Human", 122),
		("Korben Dallas", "Meat Popsicle", 100),
		("Ak'not", "Mangalore", -5)
	)
	stmt = "insert into tbl_roster(col_name, col_species, col_iq) values (?, ?, ?)"
	cur.executemany(stmt, values)
	conn.commit()

	#3) Update the Species of Korben Dallas to be Human.
	stmt = "update tbl_roster set col_species = 'Human' where col_name = 'Korben Dallas'"
	cur.execute(stmt)
	conn.commit()

	#4) Display the names and IQs of everyone in the table who is classified as Human.
	stmt = "select col_name, col_iq from tbl_roster where col_species = 'Human'"
	cur.execute(stmt)
	result = cur.fetchall()
	for row in result:
		print("{} has an IQ of {}".format(row[0], row[1]))