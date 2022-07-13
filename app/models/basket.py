from app import db
from app.models.base_entity import BaseEntity

class Basket(BaseEntity, db.Model):
    __tablename__ = "baskets"
    basketid = db.Column(db.Integer, primary_key=True)
    basketclosed = db.Column(db.Boolean, default=True, nullable=False)
    userid = db.Column(db.ForeignKey("users.userid"))
    items = db.relationship('BasketItem')

def get_items(self):
        return [item.rel_item.itemname for item in self.items]