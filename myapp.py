from flask import Flask, redirect, url_for, render_template, request, flash, session, jsonify, Blueprint
from forms import *
from flask_wtf.csrf import CSRFProtect
from config import Config
from modulos import *

app = Flask(__name__) 
csrf = CSRFProtect() # Se instancia csrf (token de seguridad para métodos POST)
csrf.init_app(app) # Se agrega csrf 
app.config.from_object(Config) #Se configura la app usando la configuración de config.py

"""
En estos momentos las vistas no hacen nada
Solo renderizan los html
"""
#vista de login
@app.route('/login')
def loginx():
	return render_template('login.html')

#vista de revisión de bulto
@app.route('/revision_bulto')
def revision_bulto():
	return render_template('revision_bulto.html')

#vista de revisión de contenido
@app.route('/revision_contenido')
def revision_contenido():
	return render_template('revision_contenido.html') 

### VISTAS DE PRUEBA

# vista de testeo de ajax la cual llama a 'servicio1'  
@app.route('/ajax')
def ajax_test():
	return render_template('ajax_test.html')

# servicio que responde a la llamada de 'ajax'
@app.route('/getproducto', methods=['GET','POST'])
def service1():
	id_producto = request.args.get('id_producto', 0, type=int)
	respuesta, mensaje = getProductById(id_producto)
	return jsonify(respuesta=respuesta, mensaje=mensaje)
	#producto, mensaje = getProductById(a)
	#return jsonify(result=producto, mensaje=mensaje)


# se corre el programa
if __name__ == '__main__':
	app.run(host="192.168.1.152",debug=True)
	#app.run(host="192.168.1.150", port="8000")



#### cosas viejas de testeo

"""
VERSIÓN ANTIGUA SIN BASE
Y usando inputs de distinta clase a 'form-control' 
form-control es la clase de input que tiene resize por defecto dependiente del tamaño de la pantalla 
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
				return render_template('login.html', error="Usuario/contraseña erroneo(s).")

	return render_template('login.html')
"""