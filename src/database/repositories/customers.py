from database import db
from database.models import Customer

def get():
    return Customer.query.all()

def create(data):
    name = data.get('name')
    email = data.get('email')
    customer_id = data.get('id')

    customer = Customer(name, email)

    if customer_id:
        customer.id = customer_id

    db.session.add(customer)
    db.session.commit()