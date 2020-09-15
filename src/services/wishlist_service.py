from database.repositories.wishlist_repository import create
from database.repositories.customer_repository import get_by_id
from database.models import Wishlist
from api.response import Response
from api.response import ResponseMessages
from tools.http_status_code import HttpStatusCode

def create_wishlist(data):
    customer_id = data.get('customer_id')
    customer = get_by_id(customer_id)

    if(customer is None):
        return Response(
        HttpStatusCode.BAD_REQUEST.value,
        ResponseMessages.ERROR.value,
        None,
        None)

    wishlist = Wishlist(customer)
    
    return Response(
        HttpStatusCode.CREATED.value,
        ResponseMessages.SUCCESS.value,
        create(wishlist),
        None)


    