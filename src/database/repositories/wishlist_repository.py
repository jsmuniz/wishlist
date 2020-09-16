from database import db
from database.models import Wishlist

def create(wishlist):
    db.session.add(wishlist)
    db.session.commit()
    db.session.refresh(wishlist)

    return wishlist

def exists_wishlist_for_customer(customer_id):
    return db.session.query(Wishlist.query.filter(Wishlist.customer_id == customer_id).exists()).scalar()



