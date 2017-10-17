from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__, template_folder='client', static_folder='client/dist')


@app.route('/commits')
def getCommits():
	with open('commits.json') as file:
		commits = file.read()
	return commits


@app.route('/commits', methods=['POST'])
def saveCommits():
	commits = request.form['commits']
	with open('commits.json', mode='w') as file:
		file.write(commits)
	return 'ok'


@app.route('/')
def index():
    return render_template('index.html')