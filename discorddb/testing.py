name = 'blueray'
field = 'blueray1'
leng = len(name)
if field == name:
	field = field + str(old + 1)
else:
	print(field[leng:])
	field = field[:leng] + str(int(field[leng:]) + 1)

print(field)