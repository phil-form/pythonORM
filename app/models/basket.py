from app import db
from app.models.base_entity import BaseEntity
<<<<<<< HEAD

class Basket(db.Model, BaseEntity):
    __tablename__ = "baskets"
    basketid = db.Column(db.Integer, primary_key=True)
    items = db.relationship('BasketItem')
=======
from app.models.basket_item import BasketItem
from app.models.item import Item


class Basket(BaseEntity, db.Model):
    __tablename__ = "baskets"
    basketid = db.Column(db.Integer, primary_key=True)
    basketclosed = db.Column(db.Boolean, nullable=False, default=False)
    userid = db.Column(db.ForeignKey('users.userid'))

    # link User.baskets member to Basket
    user = db.relationship("User", back_populates="baskets")
    items = db.relationship("BasketItem", cascade='all, delete-orphan')

    def add_item(self, item: Item, quantity: int):
        basket_item = self.find_item(item)

        exist = True

        if basket_item is None:
            exist = False
            basket_item = BasketItem()
            basket_item.item = item
            basket_item.basket = self
            self.items.append(basket_item)

        basket_item.itemquantity = quantity

        return (basket_item, exist)

    def remove_item(self, item: Item):
        basket_item = self.find_item(item)

        self.items.remove(basket_item)

    def find_item(self, item: Item):
        basket_item: BasketItem
        for basket_item in self.items:
            if item.itemid == basket_item.item.itemid:
                return basket_item
>>>>>>> main
