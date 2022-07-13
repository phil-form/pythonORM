from app import db
from app.models.base_entity import BaseEntity

class BasketItem(BaseEntity, db.Model):
    __tablename__ = "baskets_items"
    itemid = db.Column(db.ForeignKey("items.itemid"), primary_key=True)
    basketid = db.Column(db.ForeignKey("baskets.basketid"), primary_key=True)

    rel_basket = db.relationship('Basket', back_populates="items")
    rel_item = db.relationship('Item', back_populates="baskets")