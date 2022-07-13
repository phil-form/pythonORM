from app import db
from app.models.base_entity import BaseEntity

class BasketItem(db.Model, BaseEntity):
    basketid = db.Column(db.ForeignKey('baskets.basketid'), primary_key=True)
    itemid = db.Column(db.ForeignKey('items.itemid'), primary_key=True)
    itemquantity = db.Column(db.Integer, nullable=False)

    rel_basket = db.relationship('Basket', back_populates='items')
    rel_item = db.relationship('Item', back_populates='baskets')