from app.models.basket import Basket
from app.dtos.basket_dto import BasketDTO


class BasketMapper:
    @staticmethod
    def entity_to_dto(entity: Basket) -> BasketDTO:
        return BasketDTO.build_from_entity(entity)

    @staticmethod
    def form_to_entity(form, basket: Basket) -> Basket:
        pass
