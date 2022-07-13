from app import db
from app.mappers.basket_mapper import BasketMapper
from app.services.base_service import BaseService
from app.models.basket import Basket


class BasketService(BaseService):    
    def find_all(self):
        return [BasketMapper.entity_to_dto(basket) for basket in Basket.query.filter_by(active=True).all()]
    
    def find_one(self, entity_id: int):
        return BasketMapper.entity_to_dto(Basket.query.filter_by(active=True, basketid=entity_id).all())
    
    def find_one_by(self, **kwargs):
        pass

    
    def insert(self, data):
        pass

    
    def update(self, entity_id: int, data):
        pass

    
    def delete(self, entity_id: int):
        pass