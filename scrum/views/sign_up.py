import flask
from flask import session, redirect, url_for, request
import scrum

@scrum.app.route('/accounts/create', methods=['GET', 'POST'])
def show_signup():
	'''Show sign up page.'''

	# add login logic
	return flask.render_template('sign_up.html')