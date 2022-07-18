from app import db
<<<<<<< HEAD
from app.models.item import Item
from app.services.base_service import BaseService
from app.mappers.item_mapper import ItemMapper

class ItemService(BaseService):
    def find_all(self):
        return [ItemMapper.entity_to_dto(item) for item in Item.query.filter_by(active=True).all()]
    
    def find_one(self, entity_id: int):
        return ItemMapper.entity_to_dto(Item.query.filter_by(active=True, itemid= entity_id).one())
    
    def find_one_by(self, **kwargs):
        return ItemMapper.entity_to_dto(Item.query.filter_by(active=True, **kwargs).one())

    def insert(self, data: Item):
        try:
            db.session.add(data)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

        return self.find_one(data.itemid)
    
    def update(self, entity_id: int, data):
        item = Item.query.filter_by(active= True, itemid= entity_id).one()
        if item is None:
            return None

        item.itemid = data.itemid
        item.itemname = data.itemname
        item.itemprice = data.itemprice

        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

        return item

    def delete(self, entity_id: int):
        item = Item.query.filter_by(active= True, itemid= entity_id).one()
=======
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
        except:
            db.session.rollback()

        return self.find_one(item.itemid)

    def update(self, entity_id: int, data):
        item = Item.query.filter_by(itemid=entity_id).one()

        if item is None:
            return None

        ItemMapper.form_to_entity(data, item)
        try:
            db.session.commit()
        except:
            db.session.rollback()

        return self.find_one(entity_id)

    def delete(self, entity_id: int):
        item = Item.query.filter_by(itemid=entity_id).one()

>>>>>>> main
        if item is None:
            return None

        try:
            db.session.delete(item)
            db.session.commit()
<<<<<<< HEAD
        except Exception as e:
            print(e)
=======
        except:
>>>>>>> main
            db.session.rollback()

        return item.itemid