from app.models.basket import Basket
from app.dtos.item_dto import ItemDTO


class BasketDTO:
    def __init__(self, basketid, basketclosed, userid, items):
        self.basketid = basketid
        self.basketclosed = basketclosed
        self.userid = userid;
        self.basketitems = []
        for item in items:
            self.basketitems.append(ItemDTO(item.rel_item.itemid, item.rel_item.itemname, item.rel_item.itemdescription).__dict__)

    @staticmethod
    def build_from_entity(basket: Basket):
        return BasketDTO(basket.basketid, basket.basketclosed, basket.userid, basket.items)
