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
    data = environ['QUERY_STRING']
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(data)))
    ]

    start_response(status, response_headers)
    return iter([data])