from flask import render_template, session

from app import app
from app.decorators.auth_required import auth_required
from app.dtos.basket_dto import BasketDTO
from app.services.basket_service import BasketService
from app.services.item_service import ItemService
from app.services.user_service import UserService

basketService = BasketService()
itemService = ItemService()
userService = UserService()

@app.route('/basket/all')
@auth_required(level="ADMIN")
def getAllBaskets():
    return render_template('baskets/list.html', baskets=basketService.find_all())

@app.route('/basket')
@auth_required()
def getBasketDetail():
    items = itemService.find_all()
    basket = BasketDTO()
    basket.basketclosed = False
    basket.user = userService.find_one(session.get('userid'))
    return render_template('baskets/details.html',
                           basket=basket, items=items, is_basket=True)
