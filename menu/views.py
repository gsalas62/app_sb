from flask import Flask, redirect, url_for, render_template, request, session, Blueprint
from modulos import * # modulos hechos por nosotros (servicios, etc)
from .paths import Paths
from app_sb import modulos as global_modulos
from config import *

menu = Blueprint('menu',
				 __name__,
				 template_folder='templates',
   			     static_folder='static',
				 static_url_path='/%s' % __name__)

@menu.route('/menu')
def _menu():
	id_conn = session.get('id_conn', None)
	if id_conn is None:
		return redirect(url_for('login._login'))
	
	paths = Paths.apps
	tiempoMax = Timer.SEG
	contexto = global_modulos.getInfoContexto(id_conn)
	return render_template('menu.html', contexto=contexto, tiempoMax=tiempoMax)