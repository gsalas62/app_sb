import requests # Para hacer el request al servicio 
from bs4 import BeautifulSoup # Para parsear el request

"""
Testeo de login, retorna diccionario con información de contexto 
la cual es ingresada en uque se ingresa a una cookie
"""

def validateUser(user,password):

	print('alguien quiere validar!')
	url = "http://192.168.200.50:18003/soa-infra/services/RecepCiega/Serv_RegistrarLogin/bp_registrarlogin_client_ep?WSDL"
	headers = {'content-type': 'text/xml'}
	
	body = 	"""<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
					<soap:Body>
							<ns1:ParEntrada xmlns:ns1="http://www.Sqm_RegistrarLogin.org">
									<ns1:Usuario>"""+str(user)+"""</ns1:Usuario>
									<ns1:Password>"""+str(password)+"""</ns1:Password>
					</ns1:ParEntrada>
				</soap:Body>
			</soap:Envelope>"""

	# respuesta al request
	response = requests.post(url,data=body,headers=headers)
	
	# se parsea la respuesta
	soup = BeautifulSoup(str(response.content), "html.parser")

	# se buscan los tags, se obtienen sus textos y se guardan en un diccionario
	myDict = {}	
	myDict['id_conn'] = soup.find('id_conn').get_text()
	myDict['cod_status'] = soup.find('cod_status').get_text()
	myDict['msg_status'] = soup.find('msg_status').get_text()
	
	return myDict