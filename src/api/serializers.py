from flask_restplus import fields, marshal
from api.restplus import api

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

response = api.model('Response', {
    'status_code': fields.Integer(description='Request Status Code'),
    'message': fields.String(description='Request Message'),
    'details': fields.String(description='Request Details')
})


# Customer Serializers

customer = api.model('Customer', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a customer'),
    'name': fields.String(required=True, description='Customer name'),
    'email': fields.String(required=True, description='Customer e-mail'),
})

page_of_customers = api.inherit('Page of customers', pagination, {
    'items': fields.List(fields.Nested(customer))
})

customer_list_response = api.inherit('Customer List Response', response, {
    'data': fields.Nested(page_of_customers, description="A page of customers"),
})

customer_response = api.inherit('Customer Response', response, {
    'data': fields.Nested(customer, description='Customer')
})

# Wishlist Serializers

wishlist = api.model('Wishlist', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a wishlist'),
    'customer_id': fields.Integer(attribute='customer.id'),
    'customer': fields.String(attribute='customer.name'),
})

wishlist_response = api.inherit('Wishlist Response', response, {
    'data': fields.Nested(wishlist, description='Wishlist'),
})

wishlist_item = api.model('Wishlist Item', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a wishlist item'),
    'product_id': fields.String(description='Product Id'),
    'wishlist_id': fields.Integer(attribute='wishlist.id'),
    'customer': fields.String(attribute='wishlist.customer.name'),
})


wishlist_item_response = api.inherit('Wishlist Item Response', response, {
    'data': fields.Nested(wishlist_item, description='Wishlist Item'),
})

product = api.model('Product', {
    'id': fields.String(description='The unique identifier of a product'),
    'title': fields.String(description='Product title'),
    'price': fields.Float(description='Product price'),
    'image': fields.String(description='Product image link'),
    'review_score': fields.Float(description='Product review score')
})

page_of_wishlist_items = api.inherit('Page of wishlist items', pagination, {
    'items': fields.List(fields.Nested(product))
})

wishlist_items_list_response = api.inherit('Customer List Response', response, {
    'data': fields.Nested(page_of_wishlist_items, description="A page of wishlist items"),
})
