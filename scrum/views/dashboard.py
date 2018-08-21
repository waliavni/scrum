import flask
from flask import session, redirect, url_for, request
import scrum

@scrum.app.route('/dashboard', methods=['GET', 'POST'])
def show_dashboard():
	'''Show sign up page.'''

	# add login logic
	return flask.render_template('dashboard.html')