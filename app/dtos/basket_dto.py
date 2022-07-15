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

    def get_json(self):
        pass