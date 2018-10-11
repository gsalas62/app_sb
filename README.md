### Estructura del programa

``` bash
App_sb/
  |-__init__.py
  |-master.py
  |-modulos.py
  |-static/
  |-templates/
  |-login/
    |-__init__.py
    |-views.py
    |-modulos.py
    |-static/
    |-templates/
  |-menu/
    |-__init__.py
    |-views.py
    |-modulos.py
    |-static/
    |-templates
  |-revision_bultos/
    |- ...
``` 
El programa se compone de un conjunto de pequeñas aplicaciones (menu, login, revisión_bultos, etc) las cuales se definen como __blueprints__, cada una de estas aplicaciones tiene la misma estructura: un '___init_.py__', un __views.py__ y carpetas __templates/__ y __static/__ (modulos.py va dependiendo de si la aplicación usará o no métodos propios).

___init_.py__: simplemente le dice al programa base (app_sb) que esta carpeta donde está contenido corresponde a un módulo de python.
__views.py__: corresponde a la creación de un __blueprint__ junto a la vistas que tendrá la aplicación, una vista se puede definir un métodos que dado un path retorna algo con ese path (puede ser una página, puede ser un valor si es que se usó con AJAX, puede ser cualquier cosa).

Tiene la siguiente estructura:
``` python
#imports

app = Blueprint('app',__name__,template_folder='templates',static_folder='static',static_url_path='/static/')

@app.route('/path/to/this/app')
def servicio():

	""" HACER ALGO CUANDO SE ENTRE A LA PÁGINA """

  return ALGO
```
Al instanciar el blueprint hay que definir donde están sus templates y sus archivos estáticos, en otro caso tomará lo del directorio base.


Dentro de la carpeta __templates/__ se encuentran las 'planillas' o 'moldes' que usarán los métodos de la vista para renderizar las páginas, están escritos en html pero además utilizan lenguaje propio de __jinja2__ (un módulo de python para, entre otras cosas, poder enviar variables desde el método al template, más adelante se entrará en detalle de __jinja2__).

Dentro de la carpeta __static/__ se encuentra todo lo que es imágenes, css, javascript, etc, para hacer referencia dentro del template usar método __url_for('app.static', filename='path/to/file/file.[css|js|png])__, es decir si queremos hacer referencia a menu.css que se encuentra en __static/css/menu.css__ hay que agregarlo en el head (como en cualquier html) de la forma:

``` html
<link rel="stylesheet" type="text/css" href="{{ url_for('menu.static', filename='css/menu.css') }}">
```

Una vez creados los blueprints hay que agregarlos a nuestra aplicación principal, en nuestro caso se tiene el archivo __init.py__ dentro del directorio principal __app_sb__ de la forma:

``` python

```

