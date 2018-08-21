import flask
from flask import session, redirect, url_for, request
import scrum

@scrum.app.route('/editproj', methods=['GET', 'POST'])
def show_edit_proj():
	'''Show sign up page.'''

	# add login logic
	return flask.render_template('edit_project.html')