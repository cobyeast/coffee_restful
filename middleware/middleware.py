from flask import session
from werkzeug.wrappers import Request

'''
Middleware to set a 'Authorization': 'JWT Token' header in a production environment.
In production, a uWSGI file must be made with the following included -->> WSGIPassAuthorization: on
'''

class Middleware:

  def __init__(self, app):
    self.app = app

  def __call__(self, environ, start_response):
    req = Request(environ)

    print(req.headers)

    def set_jwt(status, headers):
      if '/users' in req.path and session.get('jwt'):
        print(req.path)
        headers.append(('Authorization', str('JWT' + ' ' + session.get('jwt'))))
        print(headers)
      return start_response(status, headers)

    return self.app(environ, set_jwt)