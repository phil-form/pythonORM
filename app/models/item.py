from app import db
from app.models.base_entity import BaseEntity

class Item(BaseEntity, db.Model):
    __tablename__ = "items"
    itemid = db.Column(db.Integer, primary_key=True)
    itemname = db.Column(db.String(50), nullable=False)
    itemdescription = db.Column(db.String(250))
    baskets = db.relationship('BasketItem')