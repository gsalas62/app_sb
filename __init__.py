from flask import Flask, redirect, url_for, render_template, request, flash, session, jsonify, Blueprint
from flask_wtf.csrf import CSRFProtect # protector
from config import * # config local
from modulos import * # modulos hechos por nosotros

# se instancia la app
app = Flask(__name__)

csrf = CSRFProtect() # Se instancia csrf (token de seguridad para métodos POST) 
csrf.init_app(app) # Se agrega csrf 

app.config.from_object(DevelopmentConfig) #Se configura la app usando la configuración de config.py

# se agregan los views de los blueprints
from login.views import login
from menu.views import menu
from revision_ciega.views import revision_ciega


app.register_blueprint(login)
app.register_blueprint(menu)
app.register_blueprint(revision_ciega)

"""
En estos momentos las vistas no hacen nada
Solo renderizan los html
"""

if __name__ == '__main__':
	app.run()
