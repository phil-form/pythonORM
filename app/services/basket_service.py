from app import db
from app.dtos.basket_dto import BasketDTO
from app.mappers.basket_mapper import BasketMapper
from app.models.basket import Basket
from app.services.base_service import BaseService


class BasketService(BaseService):
    def find_all(self):
        return [BasketDTO.build_from_entity(basket) for basket in Basket.query.all()]

    def find_one(self, entity_id: int):
        return BasketDTO.build_from_entity(Basket.query.filter_by(basketid=entity_id).one())

    def find_one_by(self, **kwargs):
        return BasketDTO.build_from_entity(Basket.query.filter_by(**kwargs).one())

    def insert(self, data):
        basket = Basket()
        BasketMapper.form_to_entity(data, basket)

        try:
            db.session.add(basket)
            db.session.commit()
        except:
            db.session.rollback()

        return self.find_one(basket.basketid)

    def update(self, entity_id: int, data):
        basket = Basket.query.filter_by(basketid=entity_id).one()
        if basket is None:
            return None

        BasketMapper.form_to_entity(data, basket)
        try:
            db.session.commit()
        except:
            db.session.rollback()

        return self.find_one(entity_id)

    def delete(self, entity_id: int):
        basket = Basket.query.filter_by(basketid=entity_id).one()
        if basket is None:
            return None

        try:
            db.session.delete(basket)
            db.session.commit()
        except:
            db.session.rollback()

        return basket.basketid