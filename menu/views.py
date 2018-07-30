from flask import Flask, redirect, url_for, render_template, request, session, Blueprint
from modulos import * # modulos hechos por nosotros (servicios, etc)
from .paths import Paths

menu = Blueprint('menu', __name__, template_folder='templates')

@menu.route('/menu')
def _menu():
	id_conn = session.get('id_conn', None)
	if id_conn is None:
		return redirect('login._login')
	paths = Paths.apps
	
	return render_template('menu.html', apps=paths)
