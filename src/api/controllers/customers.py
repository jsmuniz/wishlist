import logging
from flask import request
from flask_restplus import Resource
from api.serializers import customer
from api.restplus import api
import database.repositories.customers as customer_repository

log = logging.getLogger(__name__)

ns = api.namespace('customers', description='Operations related to customers')

@ns.route('/')
class CustomerCollection(Resource):

    @api.marshal_list_with(customer)
    def get(self):
        customers = customer_repository.get()
        return customers

    @api.response(201, 'Customer successfuly created')
    @api.expect(customer)
    def post(self):
        data = request.json
        customer_repository.create(data)
        return None, 201


