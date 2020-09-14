from flask_restplus import fields
from api.restplus import api

customer = api.model('Customer', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a customer'),
    'name': fields.String(required=True, description='Customer name'),
    'email': fields.String(required=True, description='Customer e-mail'),
})