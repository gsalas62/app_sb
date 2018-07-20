from flask import Flask, redirect, url_for, render_template, request, flash, session
from forms import *
from flask_wtf.csrf import CSRFProtect
from config import Config
from modulos import *

csrf = CSRFProtect()
app = Flask(__name__)
csrf.init_app(app)
app.config.from_object(Config)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	session.pop('user', None)
	# Si se entra por form
	if request.method == "POST":
		# Si el form es válido
		if form.validate():
			# user,password son los valores que están en los campos del form
			user = request.form.get('user')
			password = request.form.get('password')
			# Si las credenciales son correctas se guarda el user en una cookie y se redirecciona
			context = validateUser(user,password)
			print(context)
			if context:
				session['context'] = context
				return redirect('aplicacion1')
				#return render_template('login.html', form=form, user=user)
			# Si no, se recarga la página el error de usuario/contraseña erroneos
			else:		
				return render_template('login.html', form=form, error="Usuario/contraseña erroneo(s).")

	return render_template('login.html', form=form)

@app.route('/aplicacion1', methods=['GET', 'POST'])
def aplicacion1():
	if 'context' in session:
		form = BultosForm(request.form)
		print('Yup, entraste bien %s' %session.get('user'))
		return render_template('app1.html', form=form)
	else:
		print('no we')
		return redirect('login')

if __name__ == '__main__':
	app.run(host="192.168.1.170",port="8000")
