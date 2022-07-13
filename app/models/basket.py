from sqlalchemy import UniqueConstraint

from app import db
from app.models.base_entity import BaseEntity


class Basket(db.Model, BaseEntity):
    __tablename__ = "baskets"
    basketid = db.Column(db.Integer, primary_key=True)
    basketclosed = db.Column(db.Boolean, nullable=False, default=False)
    userid = db.Column(db.ForeignKey("users.userid"), nullable=False)
    UniqueConstraint('basketid', 'userid', name='uk_baskets_buid')
    items = db.relationship('BasketItem')
