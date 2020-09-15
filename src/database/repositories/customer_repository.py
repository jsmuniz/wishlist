from database import db
from database.models import Customer

def get(page, per_page):
    return Customer.query.paginate(page, per_page)

def get_by_id(customer_id):
    return Customer.query.filter(Customer.id == customer_id).one()

def create(data):
    name = data.get('name')
    email = data.get('email')
    customer_id = data.get('id')

    customer = Customer(name, email)

    if customer_id:
        customer.id = customer_id

    db.session.add(customer)
    db.session.commit()
    db.session.refresh(customer)

    return customer

def exists_user_with_email(email):
    return db.session.query(Customer.query.filter(Customer.email == email).exists()).scalar()


