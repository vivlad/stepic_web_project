from urlparse import parse_qs, urlparse
import os
import cgi
def app(environ, start_response):
	"""Simplest possible application object"""
	#post_env = env.copy()
	#post_env['QUERY_STRING'] = ''
	#post = cgi.FieldStorage(
	#	fp=env['wsgi.input'],
	#	environ=post_env,
	#	keep_blank_values=True
	#)
	# Returns a dictionary containing lists as values.
	#d = parse_qs(environ['QUERY_STRING'])
	#data = 'Hello, Worldss!\n'
	#url = environ['QUERY_STRING']
	#queryst = parse_qs(urlparse(url).query, keep_blank_values=True)
	#data = os.environ.get("QUERY_STRING", "No Query String in url")
	query = environ[ "QUERY_STRING" ]
	if len( query ) == 0:
		data = ''
	else:
		#data = cgi.escape( query )
		pairs = cgi.parse_qs( query )
		data = cgi.escape( query ).replace("&amp;", "\n")
		#for key, value in pairs.items():
		#	data = data + str(key) + '=' + int(str(pairs[key]).replace( "'", "" ).replace("[", "").replace("]", "")) + '\n'
	status = '200 OK'
	response_headers = [
		('Content-type','text/plain'),
		('Content-Length', str(len(data)))
	]

	start_response(status, response_headers)
	return iter([data])