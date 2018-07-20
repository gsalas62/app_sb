from flask_wtf import Form, FlaskForm
from wtforms import TextField, validators, PasswordField, BooleanField

class LoginForm(FlaskForm):
	user = TextField("Usuario: ",validators=[validators.required()])
	password = PasswordField("Contraseña: ",validators=[validators.required()])

class BultosForm(FlaskForm):
	revisar_todo = BooleanField("Revisar Todo")
	salida = TextField("Salida: ",validators=[validators.required()])
	bandeja = TextField("Bandeja: ",validators=[validators.required()])
