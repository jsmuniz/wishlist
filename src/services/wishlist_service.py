import infrastructure.products_api_http_client as http_client
from database.repositories.wishlist_repository import *
from database.repositories.customer_repository import get_by_id as get_customer_by_id
from database.repositories.wishlist_item_repository import create as create_item, exists_wishlist_product, get_paginated_wishlist_items
from database.models import Wishlist, WishlistItem
from api.response import Response
from api.response import ResponseMessages
from tools.http_status_code import HttpStatusCode
from tools.uuid_validator import is_valid_uuid


def create_wishlist(data):
    customer_id = data.get('customer_id')
    customer = get_customer_by_id(customer_id)

    validationResult = __validate_wishlist_request(customer)

    if not validationResult[0]:
        return validationResult[1]

    wishlist = Wishlist(customer)

    return Response(
        HttpStatusCode.CREATED.value,
        ResponseMessages.SUCCESS.value,
        create(wishlist),
        None)


def get_wishlist_by_customer_id(customer_id):
    return Response(
        HttpStatusCode.OK.value,
        ResponseMessages.SUCCESS.value,
        get_wishlist_by_customer(customer_id),
        None)


def add_wishlist_item(wishlist_id, data):
    wishlist = get_by_id(wishlist_id)
    product_id = data.get('product_id')

    validationResult = __validate_wishlist_item_request(wishlist, product_id)

    if not validationResult[0]:
        return validationResult[1]

    wishlist_item = WishlistItem(product_id, wishlist)

    return Response(
        HttpStatusCode.CREATED.value,
        ResponseMessages.SUCCESS.value,
        create_item(wishlist_item),
        None)


def __validate_wishlist_request(customer):
    error_message = None

    if customer is None:
        error_message = 'Invalid Customer Id'
    elif exists_wishlist_for_customer(customer.id):
        error_message = 'Customer already has a wishlist'

    return __build_validation_response(error_message)


def __validate_wishlist_item_request(wishlist, product_id):
    error_message = None

    if wishlist is None:
        error_message = 'Wishlist not found'

    elif not is_valid_uuid(product_id):
        error_message = 'Invalid Product Id'

    elif exists_wishlist_product(wishlist.id, product_id):
        error_message = 'Product already exists in the wishlist'

    elif not http_client.exists_product(product_id):
        error_message = 'Product not found'

    return __build_validation_response(error_message)


def __build_validation_response(error_message):
    if error_message is not None:
        return (False, Response(
            HttpStatusCode.BAD_REQUEST.value,
            ResponseMessages.ERROR.value,
            None,
            error_message))
    else:
        return (True, None)


def get_wishlist_items(wishlist_id, page, per_page):
    wishlist = get_by_id(wishlist_id)

    if wishlist is None:
        return Response(
            HttpStatusCode.BAD_REQUEST.value,
            ResponseMessages.ERROR.value,
            None,
            'Wishlist not found')

    products = []

    items_page = get_paginated_wishlist_items(wishlist_id, page, per_page)

    for item in items_page.items:
        products.append(http_client.get_product(item.product_id))

    items_page.items = products

    return Response(
        HttpStatusCode.OK.value,
        ResponseMessages.SUCCESS.value,
        items_page,
        None)


def delete_wishlist(wishlist_id):
    wishlist = get_by_id(wishlist_id)

    if wishlist is None:
        return Response(
            HttpStatusCode.BAD_REQUEST.value,
            ResponseMessages.ERROR.value,
            None,
            'Wishlist not found')

    delete(wishlist)

    return Response(
        HttpStatusCode.OK.value,
        ResponseMessages.SUCCESS.value,
        None,
        None)
