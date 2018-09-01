from scrum.model import get_db

def insert_user(user):
	'''Insert user into database.'''
	database = get_db()
	cursor = database.cursor()
	cursor.execute('INSERT INTO Users (first_name, last_name, email, password) VALUES (Ash, Varma, ashvarma@umich.edu, password)')
	database.commit()

def get_all_from_table(table_name):
	'''Return all data from specified table.'''
	database = get_db()
	cursor = database.cursor()
	result = cursor.execute('SELECT * FROM {}'.format(table_name))
	return result.fetchall()

# insert_row_into_table('Users', ['first_name', 'last_name', 'email'], ['Ash', 'Varma', 'ashvarma@umich.edu']) 
def insert_row_into_table(table_name, columns, data):
	'''Insert data into table_name in specified columns.'''
	database = get_db()
	cursor = database.cursor()
