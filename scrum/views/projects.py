import flask
from flask import session, redirect, url_for, request
import scrum

@scrum.app.route('/projects/', methods=['GET', 'POST'])
def show_projects():
	'''Show sign up page.'''

	# add login logic
	return flask.render_template('projects.html')