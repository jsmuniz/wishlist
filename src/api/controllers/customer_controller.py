import logging
from flask import request
from flask_restplus import Resource
from api.serializers import customer, customer_list_response, customer_response, wishlist_response, response
from api.parsers import pagination_arguments
from api.restplus import api, token_required
from services.customer_service import *
from services.wishlist_service import get_wishlist_by_customer_id

log = logging.getLogger(__name__)

ns = api.namespace('customers', description='Operations related to customers')


@ns.route('/')
class CustomerCollection(Resource):

    @api.doc(security='apikey')
    @token_required
    @api.expect(pagination_arguments)
    @api.marshal_with(customer_list_response)
    def get(self):
        args = pagination_arguments.parse_args(request)

        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        response = get_all(page, per_page)

        print(response.data)

        return response, response.status_code

    @api.doc(security='apikey')
    @token_required
    @api.response(201, 'Customer successfuly created')
    @api.expect(customer)
    @api.marshal_with(customer_response)
    def post(self):
        data = request.json
        response = create_customer(data)
        return response, response.status_code


@ns.route('/<int:id>')
class CustomerItem(Resource):

    @api.doc(security='apikey')
    @token_required
    @api.marshal_with(customer_response)
    def get(self, id):
        response = get_customer_by_id(id)
        return response, response.status_code

    @api.doc(security='apikey')
    @token_required
    @api.response(200, 'Customer successfully deleted')
    @api.marshal_with(response)
    def delete(self, id):
        response = delete_customer(id)
        return response, response.status_code

    @api.doc(security='apikey')
    @token_required
    @api.response(200, 'Customer successfully updated')
    @api.expect(customer)
    @api.marshal_with(response)
    def put(self, id):
        data = request.json
        response = update_customer(id, data)
        return response, response.status_code


@ns.route('/<int:id>/wishlists/')
class CustomerWishlists(Resource):
    @api.doc(security='apikey')
    @token_required
    @api.marshal_with(wishlist_response)
    def get(self, id):
        response = get_wishlist_by_customer_id(id)
        return response, response.status_code
