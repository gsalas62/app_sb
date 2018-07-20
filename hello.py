from flask import Flask, redirect, url_for, render_template, request, flash
from forms import *
from flask_wtf.csrf import CSRFProtect
from config import Config

csrf = CSRFProtect()
app = Flask(__name__)
csrf.init_app(app)
app.config.from_object(Config)

@app.route('/hello/<user>')
def index(user):
	return render_template('hello.html', name=user, macaco='yo')

@app.route('/', methods=['GET', 'POST'])
def testform():
	form = TestForm(request.form)
	if request.method == "POST":
		print('entraste por post we')
		field1 = request.form.get('field1')
		if form.validate():
			flash('Hola ' + field1)
	return render_template('form.html', form=form)

@app.route('/validado', methods=['POST'])
def validado():
	return 'Hola, fuiste validado men'

if __name__ == '__main__':
	app.run(host="192.168.1.170",port="5000")
