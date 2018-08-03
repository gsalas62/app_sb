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
