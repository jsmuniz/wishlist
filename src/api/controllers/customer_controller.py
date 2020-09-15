import logging
from flask import request
from flask_restplus import Resource
from api.serializers import customer, customer_list_response, customer_response
from api.parsers import pagination_arguments
from api.restplus import api
import services.customer_service as customer_service

log = logging.getLogger(__name__)

ns = api.namespace('customers', description='Operations related to customers')

@ns.route('/')
class CustomerCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(customer_list_response)
    def get(self):
        args = pagination_arguments.parse_args(request)

        page = args.get('page', 1)
        per_page = args.get('per_page', 2)

        response = customer_service.get_all(page, per_page)

        print(response.data)

        return response, response.status_code

    @api.response(201, 'Customer successfuly created')
    @api.expect(customer)
    @api.marshal_with(customer_response)
    def post(self):
        data = request.json
        response = customer_service.create_customer(data)
        return response, response.status_code


