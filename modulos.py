

def validateUser(user,password):
	if user == 'user' and password == '1234':
		mydict = {}
		mydict['user'] = 'user001'
		mydict['empresa'] = 'emp999'
		mydict['local'] = '00123'
		return mydict
		
	else:
		return False 