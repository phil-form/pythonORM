from app import db
from app.models.base_entity import BaseEntity


class Item(db.Model, BaseEntity):
    __tablename__ = "items"

    itemid = db.Column(db.Integer, primary_key=True)
    itemname = db.Column(db.String(50), unique=True, nullable=False, index=True)
    itemdescription = db.Column(db.String(255), nullable=True)

    baskets = db.relationship('BasketItem')

    def __eq__(self, other):
        return self.itemid == other.itemid and self.itemname == other.itemname
