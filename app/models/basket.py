from app import db
from app.models.base_entity import BaseEntity

class Basket(db.Model, BaseEntity):
    __tablename__ = "baskets"
    basketid = db.Column(db.Integer, primary_key=True)
    items = db.relationship('BasketItem')
