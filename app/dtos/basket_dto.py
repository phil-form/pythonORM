from app.dtos.item_dto import ItemDTO
from app.models.basket import Basket
from app.models.item import Item


class BasketDTO:
    def __init__(self, basketid, basketclosed, userid, items):
        self.basketid = basketid
        self.basketclosed = basketclosed
        self.userid = userid
        self.items = []
        for item in items:
            self.items.append(
                ItemDTO(item.rel_item.itemid, item.rel_item.itemname, item.rel_item.itemdescription, item.itemquantity
                        ).__dict__)

    def has_item(self, item: Item):
        return item in self.items

    @staticmethod
    def build_from_entity(basket: Basket):
        return BasketDTO(basket.basketid, basket.basketclosed, basket.userid, basket.items)
