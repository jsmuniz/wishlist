from database.repositories.wishlist_repository import create, exists_wishlist_for_customer
from database.repositories.customer_repository import get_by_id
from database.models import Wishlist
from api.response import Response
from api.response import ResponseMessages
from tools.http_status_code import HttpStatusCode

def create_wishlist(data):
    customer_id = data.get('customer_id')
    customer = get_by_id(customer_id)

    validationResult = __validate_customer(customer)

    if not validationResult[0]:
        return validationResult[1]

    wishlist = Wishlist(customer)
    
    return Response(
        HttpStatusCode.CREATED.value,
        ResponseMessages.SUCCESS.value,
        create(wishlist),
        None)

def __validate_customer(customer):
    error_message = None

    if customer is None:
        error_message = 'Invalid Customer Id'
    elif exists_wishlist_for_customer(customer.id):
        error_message = 'Customer already has a wishlist'

    if error_message is not None:
        return (False, Response(
        HttpStatusCode.BAD_REQUEST.value,
        ResponseMessages.ERROR.value,
        None,
        error_message))
    
    return (True, None)

    