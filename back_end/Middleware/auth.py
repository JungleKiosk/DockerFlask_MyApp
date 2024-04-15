from flask import  jsonify, Response, request
from functools import wraps
import jwt
import os

def getSessionUser(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):        
        if 'SESSION' in request.cookies:         
            try:
                request.user = jwt.decode(request.cookies['SESSION'], os.environ['SECRET_KEY'], algorithms='HS256')
                request.user['roles'] = request.user['roles'].replace("'", '').replace('[', '').replace(']', '').replace('"', '').replace(' ', '').split(',')
            except jwt.DecodeError:
                request.user = None
        else:
            request.user = None

        return f(*args, **kwargs)
    return decorated_function


def loginRequired(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):        
        try:
            if 'SESSION' in request.cookies:
                request.user = jwt.decode(request.cookies['SESSION'], os.environ['SECRET_KEY'], algorithms='HS256')
                return f(*args, **kwargs)
            else:
                return Response("", status=401)          
        except:
            return Response("", status=401)
    return decorated_function
