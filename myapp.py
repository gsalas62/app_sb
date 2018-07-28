from flask import Flask, redirect, url_for, render_template, request, flash, session, jsonify, Blueprint
from forms import *
from flask_wtf.csrf import CSRFProtect # protector
from config import * # config local
from modulos import * # modulos hechos por nosotros
import json #para parsear json que llegan como post 

app = Flask(__name__) 
csrf = CSRFProtect() # Se instancia csrf (token de seguridad para métodos POST)
csrf.init_app(app) # Se agrega csrf 
app.config.from_object(DevelopmentConfig) #Se configura la app usando la configuración de config.py

"""
En estos momentos las vistas no hacen nada
Solo renderizan los html
"""
#vista de login
@app.route('/login', methods=['POST', 'GET'])
def loginx():
	session.clear()
	return render_template('login.html')

#vista de revisión de bulto
@app.route('/revision_bulto')
def revision_bulto():
	contexto = session.get('contexto')
	id_conn = session.get('id_conn', None)
	if id_conn is None:
		return redirect('login')
		
	return render_template('revision_bulto.html', contexto=contexto)

#vista de revisión de contenido
@app.route('/revision_contenido')
def revision_contenido():
	contexto = session.get('contexto')
	id_conn = session.get('id_conn', None)
	if id_conn is None:
		return redirect('login')

	return render_template('revision_contenido.html', contexto=contexto) 

# servicio para validar login
@app.route('/validar_login', methods=['POST'])
def validar_login():
	load = request.get_json()

	# se obiene el 'nombre' del load
	user = load.get('user')
	password = load.get('password')

	# se llama el servicio y se mete a un diccionario 
	respuesta = validateUser(user,password)

	# se transforma el diccionario en un json
	info = json.dumps(respuesta, ensure_ascii=False)

	# se define el data
	data = {'data': info}

	# se manda de vuelta
	return jsonify(data)

@app.route('/set_info_contexto', methods=['POST'])
def set_info_contexto():
	load = request.get_json()

	# se obiene el 'nombre' del load
	id_conn = load.get('id_conn')

	# se llama el servicio y se mete a un diccionario 
	respuesta = getInfoContexto(id_conn)

	session['contexto'] = respuesta
	session['id_conn'] = id_conn
	
	return url_for('revision_contenido')
	# se manda de vuelta


### VISTAS DE PRUEBA

# vista de testeo de ajax la cual llama a 'servicio1' usando método GET
@app.route('/ajax')
def ajax_test():
	return render_template('ajax_test.html')

# servicio que responde a la llamada de 'ajax' usando método GET
@app.route('/getproducto', methods=['GET'])
def service1():
	id_producto = request.args.get('id_producto', 0, type=int)
	respuesta, mensaje = getProductById(id_producto)
	return jsonify(respuesta=respuesta, mensaje=mensaje)

# vista de testeo de ajax la cual llama a 'servicio' usando método POST
@app.route('/ajax_post')
def ajax_post():
	return render_template('ajax_post.html')

# servicio que recive un JSON en el request.data
# envia un diccionario en forma de JSON
@csrf.exempt
@app.route('/servicio', methods=['POST'])
def servicio():

	# se obtiene el json
	load = request.get_json()

	# se obiene el 'nombre' del load
	nombre = load.get('name')

	# se crea un diccionario 
	myDict = {}

	# se ingresan valores
	myDict['nombre'] = str(nombre)
	myDict['msg'] = 'MENSAJE'

	# se crea transforma el diccionario en un json
	info = json.dumps(myDict, ensure_ascii=False)

	# se define el data
	data = {'data': info}

	# se manda para 
	return jsonify(data)

######

@app.route('/camara')
def camara():
	return render_template('camara.html')



# se corre el programa
if __name__ == '__main__':
	app.run(host=Vars.IP, port=Vars.PORT, debug=True)
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
