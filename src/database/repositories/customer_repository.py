from database import db
from database.models import Customer


def get(page, per_page):
    return Customer.query.paginate(page, per_page)


def get_by_id(customer_id):
    return Customer.query.filter(Customer.id == customer_id).one_or_none()


def create(customer):
    db.session.add(customer)
    db.session.commit()
    db.session.refresh(customer)

    return customer


def exists_customer_with_email(email):
    return db.session.query(Customer.query.filter(Customer.email == email).exists()).scalar()


def delete(customer):
    db.session.delete(customer)
    db.session.commit()


def update(customer):
    db.session.add(customer)
    db.session.commit()


def get_customer_by_email(email):
    return Customer.query.filter(Customer.email == email).one_or_none()
