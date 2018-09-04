from scrum.model import get_db

def insert_user(user):
	'''Insert user into database.'''
	database = get_db()
	cursor = database.cursor()
	cursor.execute('INSERT INTO Users (first_name, last_name, email, password) VALUES ({})'.format(user['first_name'], 
		user['last_name'], user['email'], user['password']))
	database.commit()

def get_all_from_table(table_name):
	'''Return all data from specified table.'''
	database = get_db()
	cursor = database.cursor()
	result = cursor.execute('SELECT * FROM {}'.format(table_name))
	return result.fetchall()

# insert_row_into_table('Users', ['first_name', 'last_name', 'email'], ['Ash', 'Varma', 'ashvarma@umich.edu']) 
# ['first_name', 'last_name', 'email'] --> 'first_name, last_name, email'
def insert_row_into_table(table_name, columns, data):
	'''Insert data into table_name in specified columns.'''
	database = get_db()
	cursor = database.cursor()
	cursor.execute('INSERT INTO {} ({}) VALUES ({})'.format(table_name, col_builder(columns), data_builder(data)))
	database.commit()

def col_builder(columns):
	a = ''
	num_elements = len(columns)
	for elt in columns[0:num_elements-1:]:
		a += elt
		a += ', '
	a += columns[num_elements-1]
	return a


'''
Create a function that lets you update a table
Create a function that retrieves data from a table given a condition
Create a function that retrieves certain columns of data from a table 
'''