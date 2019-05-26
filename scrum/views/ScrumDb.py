from scrum.model import get_db


# TODO
# examples:
#
# table_name = 'Users'
# columns = ['email', 'user_id']
# condition = None
# build_select_query(table_name, columns, condition) --> 'SELECT email, user_id FROM Users'
#
# table_name = 'Users'
# columns = ['email']
# condition = 'user_id = 4'
# build_select_query(table_name, columns, condition) --> 'SELECT email FROM Users WHERE user_id = 4'
#
# table_name = 'Users'
# columns = ['email']
# condition = 'username = waliavni'
# build_select_query(table_name, columns, condition) --> 'SELECT email FROM Users WHERE username = "waliavni"'
def build_select_query(table_name, columns, condition=None):
	'''Build select query string to be executed.'''
	pass


# TODO
# examples:
#
# table_name = 'Users'
# columns = ['email', 'user_id']
# values = ['waliavni@umich.edu', 1]
# build_insert_query(table_name, columns, values) --> 'INSERT INTO Users ("email", user_id) VALUES ("waliavni@umich.edu", 1)'
#
# table_name = 'Users'
# columns = ['email']
# values = ['waliavni@umich.edu']
# build_insert_query(table_name, columns, values) --> 'INSERT INTO Users ("email") VALUES ("waliavni@umich.edu")'
def build_insert_query(table_name, columns, values):
	'''Build insert query string to be executed.'''
	pass


# TODO
# examples:
#
# table_name = 'Users'
# columns = ['email', 'user_id']
# values = ['waliavni@umich.edu', 1]
# condition = 'username = "waliavni"'
# build_update_query(table_name, columns, values, condition) --> 'UPDATE Users SET email = "waliavni@umich.edu", user_id = 1 WHERE username = "waliavni"'
#
# table_name = 'Users'
# columns = ['email']
# values = ['waliavni@umich.edu']
# condition = 'username = "waliavni"'
# build_update_query(table_name, columns, values, condition) --> 'UPDATE Users SET email = "waliavni@umich.edu" WHERE username = "waliavni"'
def build_update_query(table_name, columns, values, condition):
	'''Build update query string to be executed.'''
	pass


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

# ['Ash', 'Varma', 'ashvarma@umich.edu'] --> '"Ash", "Varma", "ashvarma@umich.edu"'
def data_builder(data):
	a = ''
	a += '"'
	num_elements = len(data)
	for elt in data[0:num_elements-1:]:
		a += elt;
		a += '", '
	a += data[num_elements-1]
	return a

#function to update a table
def table_updater(table_name, columns, data):
	pass
#function to retrieve data from a table given condition
def data_grabber_with_cond(table_name, condition):
	pass
#function to retrieve certain columns of data from a table
def data_grabber_with_col(table_name, columns):
	pass

'''
**need examples of these**
Create a function that lets you update a table
Create a function that retrieves data from a table given a condition (need clarification)
Create a function that retrieves certain columns of data from a table 
'''