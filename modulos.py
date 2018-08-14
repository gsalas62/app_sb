import requests # Para hacer el request al servicio 
from bs4 import BeautifulSoup # Para parsear el request

# getInfoContexto, método global
def getInfoContexto(id_conn):
	url = "http://192.168.200.50:18003/soa-infra/services/RecepCiega/Serv_GetInfoContexto/bp_getinfocontexto_client_ep?WSDL"
	headers = {'content-type': 'text/xml'}
	body = 	"""<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
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

	# se buscan los tags, se obtienen sus textos y se guardan en un diccionario
	myDict = {}	
	myDict['cod_status'] = soup.find('cod_status').get_text()
	myDict['msg_status'] = soup.find('msg_status').get_text().encode('unicode_escape').decode('latin1')
	#myDict['msg_status'] = soup.find('msg_status').get_text().encode('string-escape')
	myDict['Empresa'] = soup.find('empresa').get_text()
	myDict['Local'] = soup.find('local').get_text()
	myDict['Usuario'] = soup.find('usuario').get_text()

	return myDict


def RegistrarSalida(id_conn, nro_salida, rev_todo, fch_llegada, glosa):
	url = "http://192.168.200.50:18003/soa-infra/services/RecepCiega/Serv_RegistrarSalida/bp_registrarsalida_client_ep?WSDL"
	headers = {'content-type': 'text/xml'}
	body = 	"""	<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
					<soap:Body>
						<ns1:ParEntrada xmlns:ns1="http://www.Sqm_RegistrarSalida.org">
							<ns1:ID_Conn>"""+str(id_conn)+"""</ns1:ID_Conn>
							<ns1:Nro_Salida>"""+str(nro_salida)+"""</ns1:Nro_Salida>
							<ns1:Rev_Todo>"""+str(rev_todo)+"""</ns1:Rev_Todo>
							<ns1:Fch_Llegada>"""+str(fch_llegada)+"""</ns1:Fch_Llegada>
							<ns1:Glosa>"""+str(glosa)+"""</ns1:Glosa>
						</ns1:ParEntrada>
					</soap:Body>
				</soap:Envelope>"""
				

	response = requests.post(url,data=body,headers=headers)
	soup = BeautifulSoup(str(response.content), "html.parser")
	
	print(soup)
	cod_status = soup.find('cod_status').get_text()
	msg_status = soup.find('msg_status').get_text()
	
	return cod_status, msg_status