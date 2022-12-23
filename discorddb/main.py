import sqlite3
from sqlite3 import Error
import time



conn = sqlite3.connect("customers.db")
cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='data';")
exist = cur.fetchall()


sql_create_data_table = """CREATE TABLE IF NOT EXISTS data (
		id integer PRIMARY KEY AUTOINCREMENT,
		name text UNIQUE
);"""
while len(exist) < 1:
	cur.execute(sql_create_data_table)
	cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='data';")
	exist = cur.fetchall()



def all_data(table_name):
	column = '''SELECT * FROM data'''
	res = cur.execute(column)
	print(res.description)
	conn.commit()

def del_column(table_name, field):
	try:
		cur.execute(f"ALTER TABLE {table_name} DROP COLUMN {field};")
	except:
		print('it doesnt exist')

def add_column(table_name, field):
	if field[:6] == 'server':
		name = field[:6]
		number = int(field[6:])
		for i in range(number + 1):
			try:
				cur.execute(f"SELECT {name + str(i)} FROM {table_name};")
				print("done")
				conn.commit()
			except:
				cur.execute(f"ALTER TABLE {table_name} ADD COLUMN {name + str(i)} varchar(32)")
				conn.commit()
		
	else:
		cur.execute(f"ALTER TABLE {table_name} ADD COLUMN {field} varchar(32)")
		conn.commit()

def add_data(table_name, name_of_person, field, date):
	try:
		q = f'''INSERT INTO {table_name}(name,) VALUES("{name_of_person}",);'''
		cur.execute(q)
		conn.commit()
		print('commited')
	except Error as e:
		print(e)


table_name = "data"
field ="server5"
name_of_person = 'ka4ma'
date = '02/01/2022'
# add_column(table_name, field)
add_data(table_name, name_of_person, field, date)
all_data(table_name)