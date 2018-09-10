from flask import Flask, redirect, url_for, render_template, request, flash, session, jsonify, Blueprint
from app_sb import modulos as global_modulos

revision_contenido = Blueprint('revision_contenido',
								__name__,
								template_folder='templates',
								static_folder='static',
								static_url_path='/%s' % __name__)

#vista de revisión de contenido
@revision_contenido.route('/revision_contenido/')
def _revision_contenido():
	id_conn = session.get('id_conn', None)
	if id_conn is None:
		return redirect('login')
	
	contexto = global_modulos.getInfoContexto(id_conn)
	return render_template('revision_contenido.html', contexto=contexto) 
	
#servicio que llama al ValidaSalida
@revision_contenido.route('/validasalida', methods=['GET'])
def valida_salida():
	id_conn = session.get('id_conn', None)
	if id_conn is None:
		return redirect('login')
	
	nro_salida = request.args.get('nro_salida', 0, type=int)
	
	cod_status, msg_status = global_modulos.ValidaSalida(id_conn, nro_salida)
	return jsonify(cod_status=cod_status, msg_status=msg_status)
	
#servicio que llama al ValidaBandeja
@revision_contenido.route('/validabandeja', methods=['GET'])
def valida_bandeja():
	id_conn = session.get('id_conn', None)
	if id_conn is None:
		return redirect('login')
	
	nro_salida = request.args.get('nro_salida', 0, type=int)
	nro_bandeja = request.args.get('nro_bandeja', 0, type=int)
	
	cod_status, msg_status = global_modulos.ValidaBandeja(id_conn, nro_salida, nro_bandeja)
	return jsonify(cod_status=cod_status, msg_status=msg_status)
	
#servicio que llama al RegistraProducto
@revision_contenido.route('/registraproducto', methods=['GET'])
def registra_producto():
	id_conn = session.get('id_conn', None)
	if id_conn is None:
		return redirect('login')
	
	nro_salida = request.args.get('nro_salida', 0, type=int)
	nro_bandeja = request.args.get('nro_bandeja', 0, type=int)
	cod_ingresado = request.args.get('cod_ingresado', 0, type=str)
	
	cantidad, descripcion, cod_status, msg_status = global_modulos.RegistraProducto(id_conn, nro_salida, nro_bandeja, cod_ingresado)
	return jsonify(cantidad=cantidad, descripcion=descripcion, cod_status=cod_status, msg_status=msg_status)
	
#servicio que llama al RevisaContenido
@revision_contenido.route('/revisacontenido', methods=['GET'])
def revisa_contenido():
	id_conn = session.get('id_conn', None)
	if id_conn is None:
		return redirect('login')
	
	nro_salida = request.args.get('nro_salida', 0, type=int)
	nro_bandeja = request.args.get('nro_bandeja', 0, type=int)
	glosa = request.args.get('glosa', 0, type=str)
	
	cod_status, msg_status = global_modulos.RevisaContenido(id_conn, nro_salida, nro_bandeja, glosa)
	return jsonify(cod_status=cod_status, msg_status=msg_status)