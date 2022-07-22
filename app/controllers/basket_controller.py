from flask import render_template, session, request, redirect, url_for

from app import app
from app.framework.decorators.auth_required import auth_required
from app.forms.basket.basket_add_item_form import BasketAddItemForm
from app.framework.decorators.inject import inject
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
@inject
def getBasketDetail(basketService: BasketService):
    basket = basketService.find_one_by(userid=session.get('userid'), basketclosed=False)
    return render_template('baskets/details.html',
                           basket=basket, items=basket.items, is_basket=True)

@app.route('/basket/add', methods=['POST'])
@auth_required()
def add_item_to_basket():
    item_to_add = BasketAddItemForm(request.form)

    basketService.add_item(item_to_add)

    return redirect(url_for('getBasketDetail'))

@app.route('/basket/remove/<int:itemid>', methods=['POST'])
@auth_required()
def remove_item_to_basket(itemid: int):
    basketService.remove_item(itemid)

    return redirect(url_for('getBasketDetail'))

@app.route('/basket/checkout', methods=['POST'])
@auth_required()
def checkout_basket():
    basketService.checkout_basket()

    return redirect(url_for('getBasketDetail'))
