from flask import session

from app import db
from app.dtos.basket_dto import BasketDTO
from app.forms.basket.basket_add_item_form import BasketAddItemForm
from app.mappers.basket_mapper import BasketMapper
from app.models.basket import Basket
from app.models.item import Item
from app.models.user import User
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
        except Exception as e:
            print(e)
            db.session.rollback()

        return self.find_one(basket.basketid)

    def update(self, entity_id: int, data):
        basket = Basket.query.filter_by(basketid=entity_id).one()
        if basket is None:
            return None

        BasketMapper.form_to_entity(data, basket)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

        return self.find_one(entity_id)

    def delete(self, entity_id: int):
        basket = Basket.query.filter_by(basketid=entity_id).one()
        if basket is None:
            return None

        try:
            db.session.delete(basket)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

        return basket.basketid

    def add_item(self, form: BasketAddItemForm):
        userid = session.get('userid')
        item = Item.query.filter_by(itemid=int(form.itemid.data)).one()
        basket = Basket.query.filter_by(userid=userid, basketclosed=False).first()

        if basket is None:
            basket = Basket()
            print(f"\033[1;47;31mSCREAMING TEXT = {userid}  \033[0m")
            basket.user = User.query.filter_by(userid=userid).one()
            db.session.add(basket)

        basket_item, exist = basket.add_item(item, int(form.itemquantity.data))
        print(basket.__dict__)
        if not exist:
            db.session.add(basket_item)

        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            return None

        return basket

    def remove_item(self, itemid):
        userid = session.get('userid')
        item = Item.query.filter_by(itemid=itemid).one()
        basket = Basket.query.filter_by(userid=userid, basketclosed=False).first()

        if basket is None:
            return None

        try:
            basket.remove_item(item)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

    def checkout_basket(self):
        userid = session.get('userid')
        basket = Basket.query.filter_by(userid=userid, basketclosed=False).first()
        basket.basketclosed = True

        basket = Basket()
        basket.user = User.query.filter_by(userid=userid).one()
        db.session.add(basket)
        db.session.commit()
