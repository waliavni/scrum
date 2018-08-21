import flask
from flask import session, redirect, url_for, request
import scrum

@scrum.app.route('/task/view', methods=['GET', 'POST'])
def view_task():
	'''Show sign up page.'''

	# add login logic
	return flask.render_template('view_task.html')