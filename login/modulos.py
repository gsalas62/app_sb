import requests # Para hacer el request al servicio 
from bs4 import BeautifulSoup # Para parsear el request

"""
Testeo de login, retorna diccionario con información de contexto 
la cual es ingresada en uque se ingresa a una cookie
"""

def validateUser(user,password):
	print('alguien quiere validar!')
	url = "http://192.168.1.201:7106/soa-infra/services/default/Serv_RegistrarLogin/bpelprocess1_client_ep?WSDL"
	headers = {'content-type': 'text/xml'}
	body = """  <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
			    	<soap:Body>
			        	<ns1:InputPars xmlns:ns1="http://www.example.org">
	            			<ns1:ParUsuario>""" + str(user) + """</ns1:ParUsuario>
	            			<ns1:ParClave>""" +  str(password) + """</ns1:ParClave>
				        </ns1:InputPars>
				    </soap:Body>
				</soap:Envelope>"""

	# respuesta al request
	response = requests.post(url,data=body,headers=headers)
	
	# se parsea la respuesta
	soup = BeautifulSoup(str(response.content), "html.parser")

	# se buscan los tags, se obtienen sus textos y se guardan en un diccionario
	myDict = {}	
	myDict['cod_status'] = soup.find('cod_status').get_text()
	myDict['msg_status'] = soup.find('msg_status').get_text()
	myDict['id_conn'] = soup.find('id_conn').get_text()

	return myDict