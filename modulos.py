import requests # Para hacer el request al servicio 
from bs4 import BeautifulSoup # Para parsear el request


# servicio que devuelve producto dado un id
# se ingresa una url (del servicio) y se definen los headers y el body
# dentro del body se agrega el id del producto que se ingresa como argumento 
def getProductById(id_producto):
	url="http://192.168.1.201:7106/soa-infra/services/default/P1_Local/bpelprocess1_client_ep?WSDL"
	headers = {'content-type': 'text/xml'}
	body = """<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
	    	<soap:Body>
	        		<ns1:process xmlns:ns1="http://xmlns.oracle.com/Pruebas_SOA/P1_Local/BPELProcess1">
	            			<ns1:input>""" + str(id_producto) + """</ns1:input>
	        </ns1:process>
	    </soap:Body>
	</soap:Envelope>"""

	# respuesta (devuelve un html/xml)
	response = requests.post(url,data=body,headers=headers)
	print(response.content)
	# se parsea la respuesta
	soup = BeautifulSoup(str(response.content), "html.parser")

	# se busca el tag 'result' y se obtiene el texto (sin tag <result>)
	result = soup.find('result').get_text()

	# se define un mensaje de prueba
	mensaje = 1

	#testeo de alertas si producto == 'producto 1' entonces mensaje = 0
	if result == 'PRODUCTO 1':
		mensaje = 0

	# se retorna el resultado y el mensaje
	return result, mensaje



# pseudo getInfoContexto, método global
def getInfoContexto(id_conn):
	myDict = {}
	myDict['Local'] = '1'
	myDict['Empresa'] = '2'
	myDict['Usuario'] = 'PEPITO'

	return myDict

