from flask import Flask
from flask_wtf.csrf import CSRFProtect
from config import * # config local
from modulos import * # modulos hechos por nosotros
#comentario
# se instancia la app
app = Flask(__name__)
print(__name__)

# Se instancia csrf (token de seguridad para métodos POST) 
csrf = CSRFProtect() 

# Se agrega csrf a nuestra app
csrf.init_app(app)  

#Se configura la app usando la configuración de config.py
app.config.from_object(DevelopmentConfig) 

# se importan los views de los blueprints
from login.views import login
from menu.views import menu
from revision_contenido.views import revision_contenido
from revision_bultos.views import revision_bultos

# se agregan los blueprints a nuestra app
app.register_blueprint(login)
app.register_blueprint(menu)
app.register_blueprint(revision_contenido)
app.register_blueprint(revision_bultos)

