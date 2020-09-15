from database.repositories.customer_repository import get, create, exists_user_with_email
from tools.email_validator import is_valid
from api.response import Response
from api.response import ResponseMessages
from tools.http_status_code import HttpStatusCode

def get_all(page, per_page):
    return Response(
        HttpStatusCode.OK.value, 
        ResponseMessages.SUCCESS.value, 
        get(page, per_page), 
        None)

def create_customer(user):
    if is_valid(user['email']):
        if not exists_user_with_email(user['email']):
            return Response(
                HttpStatusCode.CREATED.value,
                ResponseMessages.SUCCESS.value,
                create(user),
                None)
        else:
            return Response(
            HttpStatusCode.BAD_REQUEST.value,
            ResponseMessages.ERROR.value,
            None,
            "An user with this e-mail is already registered"
        )
    else:
        return Response(
            HttpStatusCode.BAD_REQUEST.value,
            ResponseMessages.ERROR.value,
            None,
            "Invalid customer e-mail"
        )
    

    