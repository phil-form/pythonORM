from app.dtos.abstract_dto import AbstractDTO
from app.dtos.item_dto import ItemDTO
from app.dtos.user_dto import UserDTO
from app.models.basket import Basket
from copy import deepcopy


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
        basket_dto = deepcopy(self)
        basket_dto.items = [item.get_json_parsable() for item in self.items]
        basket_dto.user = self.user.get_json_parsable()

        return basket_dto.__dict__