<<<<<<< HEAD
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
=======
from app.dtos.abstract_dto import AbstractDTO
from app.dtos.item_dto import ItemDTO
from app.dtos.user_dto import UserDTO
from app.models.basket import Basket


class BasketDTO(AbstractDTO):
    def __init__(self):
        self.basketid = None
        self.basketclosed = None
        self.user = None
        self.items = []

    @staticmethod
    def build_from_entity(basket: Basket):
        basket_dto = BasketDTO()
        basket_dto.basketid = basket.basketid
        basket_dto.basketclosed = basket.basketclosed
        basket_dto.user = UserDTO.build_from_entity(basket.user)
        basket_dto.items = []

        for basket_item in basket.items:
            basket_dto.items.append(ItemDTO.build_from_entity(basket_item))

        return basket_dto

    def get_json_parsable(self):
        pass
>>>>>>> main
