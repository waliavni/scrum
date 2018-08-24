/*
	Users -> DONE
	Projects
		- Users
		- Tasks
		- Project Description
	Tasks -> DONE
		- Time to completion
		- Skills needed
		- People on it
		- Task Title
		- Timestamp
		- Task Description
		- Deadline
	Updates -> DONE
		- Update Message
		- Timestamp
		- Task associated with it
*/

CREATE TABLE Users(
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(20) NOT NULL,
	email VARCHAR(40) NOT NULL,
	user_id INTEGER PRIMARY KEY AUTOINCREMENT,
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	deleted TIMESTAMP,
	password VARCHAR(255) NOT NULL,	
	FOREIGN KEY(email) REFERENCES User_To_Id(email)
);

CREATE TABLE User_To_Id(
	email VARCHAR(40) PRIMARY KEY,
	user_id INTEGER NOT NULL,
	FOREIGN KEY(user_id) REFERENCES Users(user_id)
);

CREATE TABLE Tasks(
	task_id INTEGER PRIMARY KEY AUTOINCREMENT,
	completion TIMESTAMP NOT NULL,
	skills VARCHAR(1000) NOT NULL,
	title VARCHAR(50) NOT NULL,
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	description VARCHAR(5000) NOT NULL,
	hours_required INTEGER NOT NULL
);

CREATE TABLE TaskPermission(
	task_id INTEGER NOT NULL,
	user_id INTEGER NOT NULL,
	PRIMARY KEY(task_id, user_id),
	FOREIGN KEY(task_id) REFERENCES Tasks(task_id),
	FOREIGN KEY(user_id) REFERENCES Users(user_id)
);

CREATE TABLE TaskUpdate(
	update_id INTEGER PRIMARY KEY AUTOINCREMENT,
	task_id INTEGER NOT NULL,
	message VARCHAR(1000) NOT NULL,
	current TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	FOREIGN KEY(task_id) REFERENCES Tasks(task_id)
);

CREATE TABLE Project(
	description VARCHAR(1000) NOT NULL,
	title VARCHAR(20) NOT NULL,
	project_id INTEGER NOT NULL,
	task_id INTEGER NOT NULL,
	user_id INTEGER NOT NULL,
	PRIMARY KEY(project_id) AUTOINCREMENT,
	FOREIGN KEY(task_id) REFERENCES Tasks(task_id),
	FOREIGN KEY(user_id) REFERENCES Users(user_id)
);