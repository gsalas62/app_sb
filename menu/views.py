from flask import Flask, redirect, url_for, render_template, request, session, Blueprint
from modulos import * # modulos hechos por nosotros (servicios, etc)
from .paths import Paths
from app_sb import modulos as global_modulos

menu = Blueprint('menu',
				 __name__,
				 template_folder='templates',
   			     static_folder='static',
				 static_url_path='/static/')

@menu.route('/menu')
def _menu():
	id_conn = session.get('id_conn', None)
	if id_conn is None:
		return redirect(url_for('login._login'))
	paths = Paths.apps
	contexto = global_modulos.getInfoContexto(id_conn)
	#return render_template('menus2.html', apps=paths)
	return render_template('menu2.html', contexto=contexto)