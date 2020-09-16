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
    name = data.get('name')
    email = data.get('email')

    validation_result = __validate_fields(name, email)

    if not validation_result[0]:
        return validation_result[1]

    customer = Customer(name, email)

    return Response(
        HttpStatusCode.CREATED.value,
        ResponseMessages.SUCCESS.value,
        create(customer),
        None)

def __validate_fields(name, email):
    error_message = None

    if not name:
        error_message = "Invalid Customer Name"

    elif not is_valid(email):
        error_message = "Invalid customer e-mail"
    
    elif exists_customer_with_email(email):
        error_message = "A customer with this e-mail is already registered"

    if error_message is not None:
        return (False, Response(
            HttpStatusCode.BAD_REQUEST.value,
            ResponseMessages.ERROR.value,
            None,
            error_message))
    else:
        return (True, None)
    
