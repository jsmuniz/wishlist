import logging
import traceback

import conf
from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound
from api.response import Response, ResponseMessages
from tools.http_status_code import HttpStatusCode
from functools import wraps
from flask import request


log = logging.getLogger(__name__)

authorization = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']

        if not token:
            return {
                "status_code": HttpStatusCode.UNAUTHORIZED.value,
                "message": ResponseMessages.ERROR.value,
                "details": "Authentication token is missing"}, 401

        if token != '67c72716-f872-11ea-9cd5-635c896a9249':
            return {
                "status_code": HttpStatusCode.UNAUTHORIZED.value,
                "message": ResponseMessages.ERROR.value,
                "details": "Invalid Authentication Token"}, 401

        return f(*args, **kwargs)

    return decorated


api = Api(version='1.0', title='WishList API',
          description='Api for managing customers wishlists',
          validate=True, authorizations=authorization, security='apikey')


@api.errorhandler
def default_error_handler(e):
    return {
        "status_code": HttpStatusCode.INTERNAL_SERVER_ERROR.value,
        "message": ResponseMessages.EXCEPTION.value,
        "details": "An unexpected error occured. Consult the technical support for more details"}, 500
