from flask import Flask, redirect, url_for, render_template, request, flash, session, jsonify
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
		if request.method == "POST":
			if form.validate():
				revisar_todo = request.form.get('revisar_todo',False)
				if revisar_todo:
					print('Se tickeó')
				else:
					print('No se tickeó')
				salida = request.form.get('salida')
				bandeja = request.form.get('bandeja')
				print(revisar_todo,salida,bandeja)
				form = BultosForm()
		print('Cookie funcionando, session[\'context\']: %s.' %session.get('context'))
		return render_template('app1.html', form=form)
	else:
		print('No se detectó la cookie, se redirecciona al login')
		return redirect('login')


@app.route('/_add_numbers')
def service1():
	a = request.args.get('a', 0, type=int)
	producto = getProductById(a)
	return jsonify(result=producto)

@app.route('/ajax')
def ajax_test():
	return render_template('ajax_test.html')

if __name__ == '__main__':
	app.run(host="192.168.1.150", port="8000")
