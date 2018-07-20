import requests # Para hacer el request al servicio 
from bs4 import BeautifulSoup # Para parsear el request


def validateUser(user,password):
	if user == 'user' and password == '1234':
		mydict = {}
		mydict['user'] = 'user'
		mydict['empresa'] = 'emp999'
		mydict['local'] = 'LVA123'
		return mydict
		
	else:
		return False 

# servicio que devuelve producto dado un id
def getProductById(id_producto):
	url="http://192.168.1.201:7106/soa-infra/services/default/P1_Local/bpelprocess1_client_ep?WSDL"
	#headers = {'content-type': 'application/soap+xml'}
	headers = {'content-type': 'text/xml'}
	body = """<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
	    	<soap:Body>
	        		<ns1:process xmlns:ns1="http://xmlns.oracle.com/Pruebas_SOA/P1_Local/BPELProcess1">
	            			<ns1:input>""" + str(id_producto) + """</ns1:input>
	        </ns1:process>
	    </soap:Body>
	</soap:Envelope>"""

	# respuesta
	response = requests.post(url,data=body,headers=headers)

	# parseo
	soup = BeautifulSoup(str(response.content), "html.parser")

	# resultado sin tags
	result = soup.find('result').get_text()

	# se retorna
	return result

	# FALTA	manejar excepciones