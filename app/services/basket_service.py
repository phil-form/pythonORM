from app.mappers.basket_mapper import BasketMapper
from app.models.basket import Basket
from app.services.base_service import BaseService


class BasketService(BaseService):
    def find_all(self):
        return [BasketMapper.entity_to_dto(basket) for basket in Basket.query.filter_by(active=True).all()]

    def find_one(self, entity_id: int):
        return BasketMapper.entity_to_dto(Basket.query.filter_by(basketid=entity_id).first())

    def find_one_by(self, **kwargs):
        return BasketMapper.entity_to_dto(Basket.query.filter_by(**kwargs).first())

    def insert(self, data):
        # TODO
        pass

    def update(self, entity_id: int, data):
        # TODO
        pass

    def delete(self, entity_id: int):
        # TODO
        pass
