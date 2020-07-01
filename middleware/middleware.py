from flask import session
from werkzeug import datastructures

class Middleware:

  def __init__(self, app):
      self.app = app

  def __call__(self, environ, start_response):
    if session.get('jwt'):
      environ['Authorization'] = str('JWT' + ' ' + session.get('jwt'))
      return self.app(environ, start_response)


    # from flask import Response
    # from werkzeug.wrappers import Request

    # request = Request(environ)

    # def set_jwt(status, headers, exc_info=None):
    #   if session.get('jwt'):
    #     print(str('JWT' + ' ' + session.get('jwt')))

    #     headers.append(('Authorization', str('JWT' + ' ' + session.get('jwt'))))

    #     # res = Response(headers={'Authorization': str('JWT' + ' ' + session.get('jwt'))})

    #   return start_response(status, headers, exc_info)

    # return self.app(environ, set_jwt)



# print('path: %s, url: %s' % (request.path, request.url))

# raw_data = request.get_data(as_text=True)
# data = json.loads(raw_data)