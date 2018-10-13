from flask import Flask, redirect, url_for, render_template, request, flash, session, jsonify, Blueprint
from app_sb import modulos as global_modulos # modulos hechos por nosotros (servicios, etc)
from config import *

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
	
	tiempoMax = Timer.SEG
	contexto = global_modulos.getInfoContexto(id_conn)
	return render_template('revision_bultos.html', contexto=contexto, tiempoMax=tiempoMax)
	
#servicio que llama al RegistraSalida
@revision_bultos.route('/registrasalida', methods=['GET'])#,'POST'])
def registra_salida():
	id_conn = session.get('id_conn', None)
	if id_conn is None:
		return redirect('login')
	
	nro_salida = request.args.get('nro_salida', 0, type=int)
	rev_todo = request.args.get('rev_todo', 0, type=int)
	hora_llegada = request.args.get('hora_llegada', 0, type=str)
	
	cod_status, msg_status = global_modulos.RegistraSalida(id_conn, nro_salida, rev_todo, hora_llegada)
	return jsonify(cod_status=cod_status, msg_status=msg_status)
	
#servicio que llama al RegistraBandeja
@revision_bultos.route('/registrabandeja', methods=['GET'])
def registra_bandeja():
	id_conn = session.get('id_conn', None)
	if id_conn is None:
		return redirect('login')
	
	nro_salida = request.args.get('nro_salida', 0, type=int)
	bandeja_pub = request.args.get('bandeja_pub', 0, type=str)
	
	cant_bandejas, cod_status, msg_status = global_modulos.RegistraBandeja(id_conn, nro_salida, bandeja_pub)
	return jsonify(cant_bandejas=cant_bandejas, cod_status=cod_status, msg_status=msg_status)
	
#servicio que llama al RevisaBultos
@revision_bultos.route('/revisabultos', methods=['GET'])
def revisa_bultos():
	id_conn = session.get('id_conn', None)
	if id_conn is None:
		return redirect('login')
	
	nro_salida = request.args.get('nro_salida', 0, type=int)
	respuesta = request.args.get('respuesta', 0, type=int)
	
	link_voucher, cod_status, msg_status = global_modulos.RevisaBultos(id_conn, nro_salida, respuesta)
	return jsonify(link_voucher=link_voucher, cod_status=cod_status, msg_status=msg_status)
	
#servicio que llama al CamionRobado
@revision_bultos.route('/camionrobado', methods=['GET'])
def camion_robado():
	id_conn = session.get('id_conn', None)
	if id_conn is None:
		return redirect('login')
	
	nro_salida = request.args.get('nro_salida', 0, type=int)
	
	link_voucher, cod_status, msg_status = global_modulos.CamionRobado(id_conn, nro_salida)
	return jsonify(link_voucher=link_voucher, cod_status=cod_status, msg_status=msg_status)