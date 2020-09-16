import logging
from flask import request
from flask_restplus import Resource
from api.serializers import wishlist, wishlist_response, wishlist_item, wishlist_item_response
from api.parsers import pagination_arguments
from api.restplus import api
from services.wishlist_service import create_wishlist, add_wishlist_item

log = logging.getLogger(__name__)

ns = api.namespace('wishlists', description='Operations related to customers wishlists')

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
class WishlistItem(Resource):
    @api.response(201, 'Wishlist item successfully created.')
    @api.expect(wishlist_item)
    @api.marshal_with(wishlist_item_response)
    def post(self, id):
        data = request.json
        response = add_wishlist_item(id, data)
        return response, response.status_code


