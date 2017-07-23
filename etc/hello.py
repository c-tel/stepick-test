def wsgi_application(environ, start_response):
	status = '200 OK'
	headers = [
	('Content-type', 'text/plane')
	]
	body = ''
	qwery_str = environ.get(QUERY_STRING)
	list = qwery_str.split()
	for element in list:
		body += element + '\n' 
	start_response(status, headers)
	return body
	