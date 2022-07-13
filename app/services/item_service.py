from app.mappers.item_mapper import ItemMapper
from app.models.item import Item
from app.services.base_service import BaseService


class ItemService(BaseService):
    def find_all(self):
        return [ItemMapper.entity_to_dto(item) for item in Item.query.filter_by(active=True).all()]

    def find_one(self, entity_id: int):
        return ItemMapper.entity_to_dto(Item.query.filter_by(itemid=entity_id).first())

    def find_one_by(self, **kwargs):
        return Item.query.filter_by(**kwargs).first()

    def insert(self, data):
        pass

    def update(self, entity_id: int, data):
        pass

    def delete(self, entity_id: int):
        pass
