import logging
from flask import request
from flask_restplus import Resource
from api.serializers import wishlist, wishlist_response, wishlist_item, wishlist_item_response, wishlist_items_list_response, response
from api.parsers import pagination_arguments
from api.restplus import api
from services.wishlist_service import *

log = logging.getLogger(__name__)

ns = api.namespace(
    'wishlists', description='Operations related to customers wishlists')


@ns.route('/')
class WishlistPost(Resource):
    @api.response(201, 'Wishlist successfuly created')
    @api.expect(wishlist)
    @api.marshal_with(wishlist_response)
    def post(self):
        data = request.json
        response = create_wishlist(data)
        return response, response.status_code


@ns.route('/<int:id>')
class WishlistOperations(Resource):
    @api.response(201, 'Wishlist item successfully created')
    @api.expect(wishlist_item)
    @api.marshal_with(wishlist_item_response)
    def post(self, id):
        data = request.json
        response = add_wishlist_item(id, data)
        return response, response.status_code

    @api.expect(pagination_arguments)
    @api.response(200, 'Wishlist items successfully fetched')
    @api.marshal_with(wishlist_items_list_response)
    def get(self, id):
        args = pagination_arguments.parse_args(request)

        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        response = get_wishlist_items(id, page, per_page)
        return response, response.status_code

    @api.response(200, 'Wishlist succesfully deleted')
    @api.marshal_with(response)
    def delete(self, id):
        response = delete_wishlist(id)
        return response, response.status_code


@ns.route('/<int:id>/product/<string:product_id>')
class WishListItemOperations(Resource):
    @api.response(200, 'Wishlist item succesfully deleted')
    @api.marshal_with(response)
    def delete(self, id, product_id):
        response = delete_wishlist_item(id, product_id)
        return response, response.status_code
