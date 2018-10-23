import requests # Para hacer el request al servicio 
from bs4 import BeautifulSoup # Para parsear el request

# getInfoContexto, método global
def getInfoContexto(id_conn):
	url = "http://192.168.200.50:18003/soa-infra/services/RecepCiega/Serv_GetInfoContexto/bp_getinfocontexto_client_ep?WSDL"
	headers = {'content-type': 'text/xml'}
	body = """	<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
					<soap:Body>
						<ns1:ParEntrada xmlns:ns1="http://www.Sqm_GetInfoContexto.org">
								<ns1:ID_Conn>"""+str(id_conn)+"""</ns1:ID_Conn>
						</ns1:ParEntrada>
					</soap:Body>
				</soap:Envelope>"""
	
	# respuesta al request
	response = requests.post(url,data=body,headers=headers)
	
	# se parsea la respuesta
	soup = BeautifulSoup(str(response.content), "html.parser")
	
	# Este cod_status por defecto
	myDict = {}
	myDict['cod_status'] = 5
	
	# Esto es para verificar que efectivamente le llegó un cod_status
	res = soup.find_all('cod_status')
	if len(res) > 0:
		# se buscan los tags, se obtienen sus textos y se guardan en un diccionario
		myDict['cod_status'] = soup.find('cod_status').get_text()
		#myDict['msg_status'] = soup.find('msg_status').get_text().encode('unicode_escape').decode('latin1')
		myDict['msg_status'] = soup.find('msg_status').get_text()
		myDict['Empresa'] = soup.find('empresa').get_text()
		myDict['Local'] = soup.find('local').get_text()
		myDict['Usuario'] = soup.find('usuario').get_text()

	return myDict
	
def RegistraSalida(id_conn, nro_salida, rev_todo, hora_llegada):
	url = "http://192.168.200.50:18003/soa-infra/services/RecepCiega/Serv_RegistraSalida/bp_registrasalida_client_ep?WSDL"
	headers = {'content-type': 'text/xml'}
	body = 	"""	<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
					<soap:Body>
						<ns1:ParEntrada xmlns:ns1="http://www.Sqm_RegistraSalida.org">
								<ns1:ID_Conn>"""+str(id_conn)+"""</ns1:ID_Conn>
								<ns1:Nro_Salida>"""+str(nro_salida)+"""</ns1:Nro_Salida>
								<ns1:Rev_Todo>"""+str(rev_todo)+"""</ns1:Rev_Todo>
								<ns1:Hora_Llegada>"""+str(hora_llegada)+"""</ns1:Hora_Llegada>
						</ns1:ParEntrada>
					</soap:Body>
				</soap:Envelope>"""
	
	response = requests.post(url,data=body,headers=headers)
	soup = BeautifulSoup(str(response.content), "html.parser")
	
	# Estos datos son por defecto
	hora_llegada_o = ""
	cant_bandejas = ""
	cod_status = 5
	msg_status = ""
	
	# Esto es para verificar que efectivamente le llegó un cod_status
	res = soup.find_all('cod_status')
	if len(res) > 0:
		hora_llegada_o = soup.find('hora_llegada').get_text()
		cant_bandejas = soup.find('cant_bandejas').get_text()
		cod_status = soup.find('cod_status').get_text()
		msg_status = soup.find('msg_status').get_text()
	
	return hora_llegada_o, cant_bandejas, cod_status, msg_status
	
def RegistraBandeja(id_conn, nro_salida, bandeja_pub):
	url = "http://192.168.200.50:18003/soa-infra/services/RecepCiega/Serv_RegistraBandeja/bp_registrabandeja_client_ep?WSDL"
	headers = {'content-type': 'text/xml'}
	body = 	"""	<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
					<soap:Body>
						<ns1:ParEntrada xmlns:ns1="http://www.Sqm_RegistraBandeja.org">
								<ns1:ID_Conn>"""+str(id_conn)+"""</ns1:ID_Conn>
								<ns1:Nro_Salida>"""+str(nro_salida)+"""</ns1:Nro_Salida>
								<ns1:Bandeja_Pub>"""+str(bandeja_pub)+"""</ns1:Bandeja_Pub>
						</ns1:ParEntrada>
					</soap:Body>
				</soap:Envelope>"""
	
	response = requests.post(url,data=body,headers=headers)
	soup = BeautifulSoup(str(response.content), "html.parser")
	
	# Estos datos son por defecto
	cant_bandejas = ""
	cod_status = 5
	msg_status = ""
	
	# Esto es para verificar que efectivamente le llegó un cod_status
	res = soup.find_all('cod_status')
	if len(res) > 0:
		cant_bandejas = soup.find('cant_bandejas').get_text()
		cod_status = soup.find('cod_status').get_text()
		msg_status = soup.find('msg_status').get_text()
	
	return cant_bandejas, cod_status, msg_status
	
def ValidaSalida(id_conn, nro_salida):
	url = "http://192.168.200.50:18003/soa-infra/services/RecepCiega/Serv_ValidaSalida/bp_validasalida_client_ep?WSDL"
	headers = {'content-type': 'text/xml'}
	body = 	"""	<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
					<soap:Body>
						<ns1:ParEntrada xmlns:ns1="http://www.Sqm_ValidaSalida.org">
								<ns1:ID_Conn>"""+str(id_conn)+"""</ns1:ID_Conn>
								<ns1:Nro_Salida>"""+str(nro_salida)+"""</ns1:Nro_Salida>
						</ns1:ParEntrada>
					</soap:Body>
				</soap:Envelope>"""
	
	response = requests.post(url,data=body,headers=headers)
	soup = BeautifulSoup(str(response.content), "html.parser")
	
	# Estos datos son por defecto
	cod_status = 5
	msg_status = ""
	
	# Esto es para verificar que efectivamente le llegó un cod_status
	res = soup.find_all('cod_status')
	if len(res) > 0:
		cod_status = soup.find('cod_status').get_text()
		msg_status = soup.find('msg_status').get_text()
	
	return cod_status, msg_status
	
def ValidaBandeja(id_conn, nro_salida, bandeja_pub):
	url = "http://192.168.200.50:18003/soa-infra/services/RecepCiega/Serv_ValidaBandeja/bp_validabandeja_client_ep?WSDL"
	headers = {'content-type': 'text/xml'}
	body = 	"""	<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
					<soap:Body>
						<ns1:ParEntrada xmlns:ns1="http://www.Sqm_ValidaBandeja.org">
								<ns1:ID_Conn>"""+str(id_conn)+"""</ns1:ID_Conn>
								<ns1:Nro_Salida>"""+str(nro_salida)+"""</ns1:Nro_Salida>
								<ns1:Bandeja_Pub>"""+str(bandeja_pub)+"""</ns1:Bandeja_Pub>
						</ns1:ParEntrada>
					</soap:Body>
				</soap:Envelope>"""
	
	response = requests.post(url,data=body,headers=headers)
	soup = BeautifulSoup(str(response.content), "html.parser")
	
	# Estos datos son por defecto
	cod_status = 5
	msg_status = ""
	
	# Esto es para verificar que efectivamente le llegó un cod_status
	res = soup.find_all('cod_status')
	if len(res) > 0:
		cod_status = soup.find('cod_status').get_text()
		msg_status = soup.find('msg_status').get_text()
	
	return cod_status, msg_status
	
def RegistraProducto(id_conn, nro_salida, bandeja_pub, cod_ingresado):
	url = "http://192.168.200.50:18003/soa-infra/services/RecepCiega/Serv_RegistraProducto/bp_registraproducto_client_ep?WSDL"
	headers = {'content-type': 'text/xml'}
	body = 	"""	<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
					<soap:Body>
						<ns1:ParEntrada xmlns:ns1="http://www.Sqm_RegistraProducto.org">
								<ns1:ID_Conn>"""+str(id_conn)+"""</ns1:ID_Conn>
								<ns1:Nro_Salida>"""+str(nro_salida)+"""</ns1:Nro_Salida>
								<ns1:Bandeja_Pub>"""+str(bandeja_pub)+"""</ns1:Bandeja_Pub>
								<ns1:Cod_Ingresado>"""+str(cod_ingresado)+"""</ns1:Cod_Ingresado>
						</ns1:ParEntrada>
					</soap:Body>
				</soap:Envelope>"""
	
	response = requests.post(url,data=body,headers=headers)
	soup = BeautifulSoup(str(response.content), "html.parser")
	
	# Estos datos son por defecto
	cantidad = ""
	descripcion = ""
	cod_status = 5
	msg_status = ""
	
	# Esto es para verificar que efectivamente le llegó un cod_status
	res = soup.find_all('cod_status')
	if len(res) > 0:
		cantidad = soup.find('cantidad').get_text()
		descripcion = soup.find('descripcion').get_text()
		cod_status = soup.find('cod_status').get_text()
		msg_status = soup.find('msg_status').get_text()
	
	return cantidad, descripcion, cod_status, msg_status
	
def RevisaBultos(id_conn, nro_salida, respuesta):
	url = "http://192.168.200.50:18003/soa-infra/services/RecepCiega/Serv_RevisaBultos/bp_revisabultos_client_ep?WSDL"
	headers = {'content-type': 'text/xml'}
	body = 	"""	<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
					<soap:Body>
						<ns1:ParEntrada xmlns:ns1="http://www.Sqm_RevisaBultos.org">
								<ns1:ID_Conn>"""+str(id_conn)+"""</ns1:ID_Conn>
								<ns1:Nro_Salida>"""+str(nro_salida)+"""</ns1:Nro_Salida>
								<ns1:Respuesta>"""+str(respuesta)+"""</ns1:Respuesta>
						</ns1:ParEntrada>
					</soap:Body>
				</soap:Envelope>"""
	
	response = requests.post(url,data=body,headers=headers)
	soup = BeautifulSoup(str(response.content), "html.parser")
	
	# Estos datos son por defecto
	link_voucher = ""
	cod_status = 5
	msg_status = ""
	
	# Esto es para verificar que efectivamente le llegó un cod_status
	res = soup.find_all('cod_status')
	if len(res) > 0:
		link_voucher = soup.find('link_voucher').get_text()
		cod_status = soup.find('cod_status').get_text()
		msg_status = soup.find('msg_status').get_text()
	
	return link_voucher, cod_status, msg_status
	
def CamionRobado(id_conn, nro_salida):
	url = "http://192.168.200.50:18003/soa-infra/services/RecepCiega/Serv_CamionRobado/bp_camionrobado_client_ep?WSDL"
	headers = {'content-type': 'text/xml'}
	body = 	"""	<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
					<soap:Body>
						<ns1:ParEntrada xmlns:ns1="http://www.Sqm_CamionRobado.org">
								<ns1:ID_Conn>"""+str(id_conn)+"""</ns1:ID_Conn>
								<ns1:Nro_Salida>"""+str(nro_salida)+"""</ns1:Nro_Salida>
						</ns1:ParEntrada>
					</soap:Body>
				</soap:Envelope>"""
	
	response = requests.post(url,data=body,headers=headers)
	soup = BeautifulSoup(str(response.content), "html.parser")
	
	# Estos datos son por defecto
	link_voucher = ""
	cod_status = 5
	msg_status = ""
	
	# Esto es para verificar que efectivamente le llegó un cod_status
	res = soup.find_all('cod_status')
	if len(res) > 0:
		link_voucher = soup.find('link_voucher').get_text()
		cod_status = soup.find('cod_status').get_text()
		msg_status = soup.find('msg_status').get_text()
	
	return link_voucher, cod_status, msg_status
	
def RevisaContenido(id_conn, nro_salida, bandeja_pub, glosa):
	url = "http://192.168.200.50:18003/soa-infra/services/RecepCiega/Serv_RevisaContenido/bp_revisacontenido_client_ep?WSDL"
	headers = {'content-type': 'text/xml'}
	body = 	"""	<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
					<soap:Body>
						<ns1:ParEntrada xmlns:ns1="http://www.Sqm_RevisaContenido.org">
								<ns1:ID_Conn>"""+str(id_conn)+"""</ns1:ID_Conn>
								<ns1:Nro_Salida>"""+str(nro_salida)+"""</ns1:Nro_Salida>
								<ns1:Bandeja_Pub>"""+str(bandeja_pub)+"""</ns1:Bandeja_Pub>
								<ns1:Glosa>"""+str(glosa)+"""</ns1:Glosa>
						</ns1:ParEntrada>
					</soap:Body>
				</soap:Envelope>"""
	
	response = requests.post(url,data=body,headers=headers)
	soup = BeautifulSoup(str(response.content), "html.parser")
	
	# Estos datos son por defecto
	cod_status = 5
	msg_status = ""
	
	# Esto es para verificar que efectivamente le llegó un cod_status
	res = soup.find_all('cod_status')
	if len(res) > 0:
		cod_status = soup.find('cod_status').get_text()
		msg_status = soup.find('msg_status').get_text()
	
	return cod_status, msg_status
	
def CancelaRevContenido(id_conn, nro_salida, bandeja_pub):
	url = "http://192.168.200.50:18003/soa-infra/services/RecepCiega/Serv_CancelaRevContenido/bp_cancelarevcontenido_client_ep?WSDL"
	headers = {'content-type': 'text/xml'}
	body = 	"""	<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
					<soap:Body>
						<ns1:ParEntrada xmlns:ns1="http://www.Sqm_CancelaRevContenido.org">
								<ns1:ID_Conn>"""+str(id_conn)+"""</ns1:ID_Conn>
								<ns1:Nro_Salida>"""+str(nro_salida)+"""</ns1:Nro_Salida>
								<ns1:Bandeja_Pub>"""+str(bandeja_pub)+"""</ns1:Bandeja_Pub>
						</ns1:ParEntrada>
					</soap:Body>
				</soap:Envelope>"""
	
	response = requests.post(url,data=body,headers=headers)
	soup = BeautifulSoup(str(response.content), "html.parser")
	
	# Estos datos son por defecto
	cod_status = 5
	msg_status = ""
	
	# Esto es para verificar que efectivamente le llegó un cod_status
	res = soup.find_all('cod_status')
	if len(res) > 0:
		cod_status = soup.find('cod_status').get_text()
		msg_status = soup.find('msg_status').get_text()
	
	return cod_status, msg_status