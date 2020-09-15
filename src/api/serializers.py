from flask_restplus import fields, marshal
from api.restplus import api

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})


customer = api.model('Customer', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a customer'),
    'name': fields.String(required=True, description='Customer name'),
    'email': fields.String(required=True, description='Customer e-mail'),
})

page_of_customers = api.inherit('Page of blog posts', pagination, {
    'items': fields.List(fields.Nested(customer))
})

customer_list_response = api.model('Customer List Response', {
    'status_code': fields.Integer(description='Request Status Code'),
    'message': fields.String(description='Request Message'), 
    'data': fields.Nested(page_of_customers, description="A page of customers"),
    'details': fields.String(description='Request Details')
})

customer_response = api.model('Customer Response', {
    'status_code': fields.Integer(description='Request Status Code'),
    'message': fields.String(description='Request Message'), 
    'data': fields.Nested(customer, description='Customer'),
    'details': fields.String(description='Request Details')
})