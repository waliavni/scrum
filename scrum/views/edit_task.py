import flask
from flask import session, redirect, url_for, request
import scrum

@scrum.app.route('/task/edit/', methods=['GET', 'POST'])
def show_edit_task():
	'''Show sign up page.'''

	# add login logic
	return flask.render_template('edit_task.html')