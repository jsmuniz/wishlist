from database import db
from database.models import Wishlist

def create(wishlist):
    db.session.add(wishlist)
    db.session.commit()
    db.session.refresh(wishlist)

    return wishlist

def get_by_id(wishlist_id):
    return Wishlist.query.filter(Wishlist.id == wishlist_id).one_or_none()

def get_wishlist_by_customer(customer_id):
    return Wishlist.query.filter(Wishlist.customer_id == customer_id).one_or_none()

def exists_wishlist_for_customer(customer_id):
    return db.session.query(Wishlist.query.filter(Wishlist.customer_id == customer_id).exists()).scalar()

def exists_wishlist(wishlist_id):
        return db.session.query(Wishlist.query.filter(Wishlist.id == wishlist_id).exists()).scalar()
        




