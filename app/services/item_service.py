import datetime

from app import db
from app.dtos.item_dto import ItemDTO
from app.mappers.item_mapper import ItemMapper
from app.models.item import Item
from app.services.base_service import BaseService


class ItemService(BaseService):
    def find_all(self):
        return [ItemDTO.build_from_entity(item) for item in Item.query.all()]

    def find_one(self, entity_id: int):
        return ItemDTO.build_from_entity(Item.query.filter_by(itemid=entity_id).one())

    def find_one_by(self, **kwargs):
        return ItemDTO.build_from_entity(Item.query.filter_by(**kwargs).one())

    def insert(self, data):
        item = Item()
        ItemMapper.form_to_entity(data, item)

        try:
            db.session.add(item)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

        return self.find_one(item.itemid)

    def update(self, entity_id: int, data):
        item = Item.query.filter_by(itemid=entity_id).one()

        if item is None:
            return None

        ItemMapper.form_to_entity(data, item)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()

        return self.find_one(entity_id)

    def delete(self, entity_id: int):
        item = Item.query.filter_by(itemid=entity_id).one()

        if item is None:
            return None

        try:
            db.session.delete(item)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

        return item.itemid