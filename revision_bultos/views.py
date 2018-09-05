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
	
#servicio que llama al RegistraSalida
@revision_bultos.route('/registrasalida', methods=['GET'])#,'POST'])
def registra_salida():
	id_conn = session.get('id_conn', None)
	if id_conn is None:
		return redirect('login')
	
	nro_salida = request.args.get('nro_salida', 0, type=int)
	rev_todo = request.args.get('rev_todo', 0, type=int)
	fch_llegada = request.args.get('fch_llegada', 0, type=str)#'2018-08-13T12:20:32'
	glosa = request.args.get('glosa', 0, type=str)#'Algun Commentario Serv'
	
	cod_status, msg_status = global_modulos.RegistraSalida(id_conn, nro_salida, rev_todo, fch_llegada, glosa)
	return jsonify(cod_status=cod_status, msg_status=msg_status)
	
#servicio que llama al RegistraBandeja
@revision_bultos.route('/registrabandeja', methods=['GET'])
def registra_bandeja():
	id_conn = session.get('id_conn', None)
	if id_conn is None:
		return redirect('login')
	
	nro_salida = request.args.get('nro_salida', 0, type=int)
	nro_bandeja = request.args.get('nro_bandeja', 0, type=int)
	glosa = request.args.get('glosa', 0, type=str)
	
	cant_bandejas, cod_status, msg_status = global_modulos.RegistraBandeja(id_conn, nro_salida, nro_bandeja, glosa)
	return jsonify(cant_bandejas=cant_bandejas, cod_status=cod_status, msg_status=msg_status)
	
#servicio que llama al RevisaBultos
@revision_bultos.route('/revisabultos', methods=['GET'])
def revisa_bultos():
	id_conn = session.get('id_conn', None)
	if id_conn is None:
		return redirect('login')
	
	nro_salida = request.args.get('nro_salida', 0, type=int)
	respuesta = request.args.get('respuesta', 0, type=int)
	
	link_boucher, cod_status, msg_status = global_modulos.RevisaBultos(id_conn, nro_salida, respuesta)
	return jsonify(link_boucher=link_boucher, cod_status=cod_status, msg_status=msg_status)
	
#servicio que llama al CamionRobado
@revision_bultos.route('/camionrobado', methods=['GET'])
def camion_robado():
	id_conn = session.get('id_conn', None)
	if id_conn is None:
		return redirect('login')
	
	nro_salida = request.args.get('nro_salida', 0, type=int)
	
	link_boucher, cod_status, msg_status = global_modulos.CamionRobado(id_conn, nro_salida)
	return jsonify(link_boucher=link_boucher, cod_status=cod_status, msg_status=msg_status)