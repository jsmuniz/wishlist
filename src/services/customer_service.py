from database.repositories.customer_repository import *
from database.repositories.wishlist_repository import exists_wishlist_for_customer
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


def get_customer_by_id(customer_id):
    return Response(
        HttpStatusCode.OK.value,
        ResponseMessages.SUCCESS.value,
        get_by_id(customer_id),
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


def delete_customer(customer_id):
    customer = get_by_id(customer_id)

    validation_result = __validate_delete_customer_request(customer)

    if not validation_result[0]:
        return validation_result[1]

    return Response(
        HttpStatusCode.OK.value,
        ResponseMessages.SUCCESS.value,
        delete(customer),
        None)


def __validate_delete_customer_request(customer):
    error_message = None

    if customer is None:
        error_message = 'Customer not found'

    if error_message is not None:
        return (False, Response(
            HttpStatusCode.BAD_REQUEST.value,
            ResponseMessages.ERROR.value,
            None,
            error_message
        ))

    return (True, None)


def update_customer(customer_id, data):
    customer = get_by_id(customer_id)
    name = data.get('name')
    email = data.get('email')

    validation_result = __validate_update_customer_request(
        customer, name, email)

    if not validation_result[0]:
        return validation_result[1]

    customer.name = name
    customer.email = email

    return Response(
        HttpStatusCode.OK.value,
        ResponseMessages.SUCCESS.value,
        update(customer),
        None)


def __validate_update_customer_request(customer, name, email):
    error_message = None

    if customer is None:
        error_message = "Customer not found"

    elif not name:
        error_message = "Invalid customer name"

    elif not is_valid(email):
        error_message = "Invalid customer e-mail"

    else:
        customer_with_same_email = get_customer_by_email(email)
        if customer_with_same_email is not None and customer_with_same_email.id != customer.id:
            error_message = "A customer with this e-mail is already registered"

    if error_message:
        return (False, Response(
            HttpStatusCode.BAD_REQUEST.value,
            ResponseMessages.ERROR.value,
            None,
            error_message
        ))

    return (True, None)
