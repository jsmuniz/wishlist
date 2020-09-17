from database import db


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email


class Wishlist(db.Model):
    __tablename__ = 'wishlists'

    id = db.Column(db.Integer, primary_key=True)

    customer_id = db.Column(db.Integer, db.ForeignKey(
        'customers.id', ondelete="cascade"), unique=True)
    customer = db.relationship(
        'Customer', backref=db.backref('wishlists', lazy='dynamic'))

    def __init__(self, customer):
        self.customer = customer


class WishlistItem(db.Model):
    __tablename__ = 'wishlist_items'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(50), unique=True, nullable=False)

    wishlist_id = db.Column(db.Integer, db.ForeignKey(
        'wishlists.id', ondelete="cascade"), unique=False)
    wishlist = db.relationship('Wishlist', backref=db.backref(
        'wishlist_itens', lazy='dynamic'))

    def __init__(self, product_id, wishlist):
        self.product_id = product_id
        self.wishlist = wishlist
