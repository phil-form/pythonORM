from app.models.item import Item
from app.dtos.item_dto import ItemDTO

class ItemMapper:
    def entity_to_dto(entity: Item):
        return ItemDTO.build_from_entity(entity)
