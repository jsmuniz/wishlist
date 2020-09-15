from database.repositories.customer_repository import get, create, exists_customer_with_email
from tools.email_validator import is_valid
from api.response import Response
from api.response import ResponseMessages
from tools.http_status_code import HttpStatusCode
from database.models import Customer

def get_all(page, per_page):
    return Response(
        HttpStatusCode.OK.value, 
        ResponseMessages.SUCCESS.value, 
        get(page, per_page), 
        None)

def create_customer(data):
    if is_valid(data['email']):
        if not exists_customer_with_email(data['email']):
            name = data.get('name')
            email = data.get('email')

            customer = Customer(name, email)

            return Response(
                HttpStatusCode.CREATED.value,
                ResponseMessages.SUCCESS.value,
                create(customer),
                None)
        else:
            return Response(
            HttpStatusCode.BAD_REQUEST.value,
            ResponseMessages.ERROR.value,
            None,
            "A customer with this e-mail is already registered"
        )
    else:
        return Response(
            HttpStatusCode.BAD_REQUEST.value,
            ResponseMessages.ERROR.value,
            None,
            "Invalid customer e-mail"
        )
    

    