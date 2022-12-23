import sqlite3

conn = sqlite3.connect('data.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS customers (
		id integer PRIMARY KEY AUTOINCREMENT,
		name text UNIQUE
);""")

# def add_data(name, field, date):
# 	with conn:
# 		command = f"INSERT INTO customers(name, {field}) VALUES ('{name}','{date}')"
# 		c.execute(command)

def add_data(name, field, date):
	with conn:
		command = f"INSERT INTO customers (name, {field}) VALUES ('{name}', '{date}') ON CONFLICT (name) DO UPDATE SET {field}=excluded.{field}"
		c.execute(command)

def search_name(name):
	with conn:
		c.execute("SELECT * FROM customers WHERE name=?", (name,))
		return c.fetchone()

def remove_row(name):
	with conn:
		c.execute("DELETE from customers WHERE name=?", (name,))

def all_data():
	with conn:
		c.execute("SELECT * FROM customers")
		return c.fetchall()

def add_column(field):
	if field[:6] == 'server':
		name = field[:6]
		number = int(field[6:])
		for i in range(number + 1):
			try:
				command = f"SELECT {name + str(i)} FROM customers"
				c.execute(command)
				conn.commit()
			except:
				command = f"ALTER TABLE customers ADD COLUMN {name + str(i)} varchar(32)"
				c.execute(command)
				conn.commit()

def remove_column(field):
	try:
		with conn:
			command = f"ALTER TABLE customers DROP COLUMN {field}"
			c.execute(command)
	except:
		return 'field doesnt exist'

def get_columns():
	try:
		with conn:
			command = "SELECT name FROM pragma_table_info('customers')"
			c.execute(command)
			data = c.fetchall()
			return data
	except:
		return "Table doesnt exist"


name ='ka4ma'
field = 'server20'
date = '09/01/2022'
print(search_name('ka4ma'))
# add_column(field)
#add_data(name, field, date)
#remove_column(field)
#print(all_data())
# columnns = get_columns()
# print(columnns[0])
conn.close()