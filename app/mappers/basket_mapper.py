from app.models.basket import Basket
from app.dtos.basket_dto import BasketDTO

class BasketMapper:
    def entity_to_dto(entity: Basket):
        return BasketDTO.build_from_entity(entity)