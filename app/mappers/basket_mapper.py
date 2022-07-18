from app.dtos.basket_dto import BasketDTO
from app.forms.basket.basket_add_item_form import BasketAddItemForm
from app.mappers.abstract_mapper import AbstractMapper
from app.models.basket import Basket


class BasketMapper(AbstractMapper):
    @staticmethod
    def entity_to_dto(entity: Basket):
        return BasketDTO.build_from_entity(entity)

    @staticmethod
    def form_to_entity(form, basket: Basket):
        pass
        # if isinstance(form, BasketAddItemForm):
        #
