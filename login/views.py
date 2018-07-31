from flask import Flask, redirect, url_for, render_template, request, flash, session, jsonify, Blueprint
from flask_wtf.csrf import CSRFProtect # protector para POST request
from .modulos import validateUser
import json

login = Blueprint('login',
				  __name__,
				  template_folder='templates',
				  static_folder='static',
				  static_url_path='/static/')

#vista de login
@login.route('/login')
def _login():
	# borra todas las cookies al entrar
	session.clear()
	# renderiza template
	return render_template('login.html')
	
# método que es llamado por ajax desde template login.html
# devuelve cod_status y msg_status si es que no se puede validar
# devuelve la url del menú y crea cookie 'id_conn' si es que logra acceder

@login.route('/validar_login', methods=['POST'])
def validar_login():

	load = request.get_json()

	print('validar login')
	# se obiene el 'nombre' del load
	user = load.get('user')
	password = load.get('password')

	# se llama el servicio y se mete a un diccionario 
	respuesta = validateUser(user,password)
	print(respuesta)
	
	if respuesta.get('cod_status') == '0':
		session['id_conn'] = respuesta.get('id_conn')
		url = {'url': url_for('menu._menu') }
		info = json.dumps(url, ensure_ascii=False)
		data = {'data': info}
		return jsonify(data)

	# se transforma el diccionario en un json
	info = json.dumps(respuesta, ensure_ascii=False)

	# se define el data
	data = {'data': info}
	# se manda de vuelta
	return jsonify(data)