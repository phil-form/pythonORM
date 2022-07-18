from app import db
from app.models.base_entity import BaseEntity


class Basket(BaseEntity, db.Model):
    __tablename__ = "baskets"
    basketid = db.Column(db.Integer, primary_key=True)
    basketclosed = db.Column(db.Boolean, nullable=False, default=False)
    userid = db.Column(db.ForeignKey('users.userid'))

    # link User.baskets member to Basket
    user = db.relationship("User", back_populates="baskets")
    items = db.relationship("BasketItem", cascade='delete, delete-orphan')