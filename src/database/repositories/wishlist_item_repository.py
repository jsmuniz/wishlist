from database import db
from database.models import WishlistItem


def create(wishlist_item):
    db.session.add(wishlist_item)
    db.session.commit()
    db.session.refresh(wishlist_item)

    return wishlist_item


def exists_wishlist_product(wishlist_id, product_id):
    filter = WishlistItem.query.filter(
        WishlistItem.wishlist_id == wishlist_id, WishlistItem.product_id == product_id).exists()
    return db.session.query(filter).scalar()


def get_paginated_wishlist_items(wishlist_id, page, per_page):
    return WishlistItem.query.filter(WishlistItem.wishlist_id == wishlist_id).paginate(page, per_page)
