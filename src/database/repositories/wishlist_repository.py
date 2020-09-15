from database import db
from database.models import Wishlist

def create(wishlist):
    db.session.add(wishlist)
    db.session.commit()
    db.session.refresh(wishlist)

    return wishlist



