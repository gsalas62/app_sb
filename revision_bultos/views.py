from flask import Flask, redirect, url_for, render_template, request, flash, session, jsonify, Blueprint
#from flask_wtf.csrf import CSRFProtect # protector para POST request
from app_sb import modulos as global_modulos # modulos hechos por nosotros (servicios, etc)
#import json # para manejar json's

revision_bultos = Blueprint('revision_bultos',
						   __name__,
						   template_folder='templates',
						   static_folder='static',
						   static_url_path='/%s' % __name__)

#vista de revision de bultos
@revision_bultos.route('/revision_bultos/')
def _revision_bultos():
	id_conn = session.get('id_conn', None)
	if id_conn is None:
		return redirect('login')

	contexto = global_modulos.getInfoContexto(id_conn)

	return render_template('revision_bultos.html', contexto=contexto)

#servicio que llama al registrar salida
@revision_bultos.route('/registrarsalida', methods=['GET','POST'])
def registrar_salida():
	id_conn = session.get('id_conn', None)
	if id_conn is None:
		return redirect('login')
	
	nro_salida = request.args.get('nro_salida', 0, type=int)
	rev_todo = request.args.get('rev_todo', 0, type=int)
	fch_llegada = '2018-08-13T12:20:32'
	glosa = 'Algun Commentario Serv'
	
	cod_status, msg_status = global_modulos.RegistrarSalida(id_conn, nro_salida, rev_todo, fch_llegada, glosa)
	return jsonify(cod_status=cod_status,  msg_status=msg_status)