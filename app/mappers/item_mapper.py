from app.dtos.item_dto import ItemDTO
from app.models.item import Item


class ItemMapper:
    @staticmethod
    def entity_to_dto(entity: Item) -> ItemDTO:
        return ItemDTO.build_from_entity(entity)
