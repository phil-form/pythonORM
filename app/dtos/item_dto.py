from app.dtos.abstract_dto import AbstractDTO
from app.models.basket_item import BasketItem
from app.models.item import Item


class ItemDTO(AbstractDTO):
    def __init__(self):
        self.itemid = None
        self.itemname = None
        self.itemdescription = None
        self.itemquantity = None

    @staticmethod
    def build_from_entity(entity):
        item_dto = ItemDTO()

        if isinstance(entity, Item):
            item_dto.itemid = entity.itemid
            item_dto.itemname = entity.itemname
            item_dto.itemquantity = entity.itemstock
            item_dto.itemdescription = entity.itemdescription
        elif isinstance(entity, BasketItem):
            item_dto.itemid = entity.item.itemid
            item_dto.itemname = entity.item.itemname
            item_dto.itemquantity = entity.itemquantity
            item_dto.itemdescription = entity.item.itemdescription

        return item_dto


    def get_json_parsable(self):
        return self.__dict__
