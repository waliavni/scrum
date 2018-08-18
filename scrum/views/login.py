import flask
from flask import session, redirect, url_for, request
import scrum

@scrum.app.route('/accounts/login/', methods=['GET', 'POST'])
def show_login():
	'''Show sign up page.'''

	# add login logic
	return flask.render_template('login.html')