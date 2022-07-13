from app import db
from app.models.basket import Basket
from app.models.item import Item
from app.services.base_service import BaseService
from app.mappers.basket_mapper import BasketMapper


class BasketService(BaseService):
    def find_all(self):
        return [BasketMapper.entity_to_dto(basket) for basket in Basket.query.filter_by(active=True).all()]

    def find_all_no_dto(self):
        return Basket.query.all()

    def find_one(self, entity_id: int):
        return BasketMapper.entity_to_dto(Basket.query.filter_by(basketid=entity_id).first())

    def find_one_by(self, **kwargs) -> Basket:
        return User.query.filter_by(**kwargs).first()

    def insert(self, data: Basket):
        try:
            db.session.add(data)
            db.session.commit()
        except:
            db.session.rollback()

        return self.find_one(data.basketid)

    def update(self, entity_id: int, data: Basket):
        basket = Basket.query.filter_by(basketid=entity_id).first()
        basket.bascketclosed = data.basketclosed

        item_basket = Item.query.filter_by(rolename="USER").one()
        basket.add_role(item_basket)

        try:
            db.session.commit()
        except:
            db.session.rollback()
            return None

        return BasketMapper.entity_to_dto(basket)

    def delete(self, entity_id: int):
        basket = Basket.query.filter_by(basketid=entity_id).first()

        if basket is not None:
            db.session.delete(basket)
            db.session.commit()

        return basket.basketid