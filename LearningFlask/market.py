from flask import Flask
from flask import render_template


app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home_page():
	return render_template('home.html')
@app.route('/projects.html')
@app.route('/projects')
def proj():
	items= [
		{'proj':'Discord Invite Joiner', 'date':'04/11/2021', 'eff':3.5, 'rate':3.5}
	]

	return render_template('Projects.html', items=items)

@app.route('/about')
@app.route('/aboutme')
@app.route('/about_me')
@app.route('/about.html')
@app.route('/aboutme.html')
@app.route('/about_me.html')
def about():
	return render_template('about_me.html')


@app.route('/contacts')
@app.route('/contact')
@app.route('/contacts.html')
@app.route('/contact.html')
def contacts():
	return render_template('contacts.html')

app.run(debug=True)
