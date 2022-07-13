from app.models.basket import Basket
from app.models.item import Item
from app.dtos.item_dto import ItemDTO

class BasketDTO:
    def __init__(self, basketid):
        self.basketid = basketid
        self.items = self.get_items()

    def get_items(self):
        return [ItemDTO.build_from_entity(item) for item in Item.query.filter_by(basketid=self.basketid, active=True).all()]

    @staticmethod
    def build_from_entity(basket: Basket):
        return BasketDTO(basket.basketid)