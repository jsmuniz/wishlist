import logging
import traceback

import conf
from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound
from api.response import Response, ResponseMessages
from tools.http_status_code import HttpStatusCode

log = logging.getLogger(__name__)

api = Api(version='1.0', title='WishList API',
          description='Api for managing customers wishlists')


@api.errorhandler
def default_error_handler(e):
    response = Response(
        HttpStatusCode.INTERNAL_SERVER_ERROR.value,
        ResponseMessages.EXCEPTION.value,
        None,
        None)

    return {message: 'DEU RUIM'}, response.status_code