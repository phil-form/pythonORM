from flask import jsonify, render_template, session, request, redirect, url_for

from app import app
from app.framework.decorators.auth_required import auth_required
from app.framework.decorators.inject import inject

from app.forms.basket.basket_add_item_form import BasketAddItemForm
from app.services.basket_service import BasketService

@app.route('/basket/all')
@auth_required(level="ADMIN")
@inject
def getAllBaskets(basketService: BasketService):
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
@inject
def add_item_to_basket(basketService: BasketService):
    item_to_add = BasketAddItemForm(request.form)

    basketService.add_item(item_to_add)

    return redirect(url_for('getBasketDetail'))

@app.route('/basket/remove/<int:itemid>', methods=['POST'])
@auth_required()
@inject
def remove_item_to_basket(basketService: BasketService, itemid: int):
    basketService.remove_item(itemid)

    return redirect(url_for('getBasketDetail'))

@app.route('/basket/checkout', methods=['POST'])
@auth_required()
@inject
def checkout_basket(basketService: BasketService):
    basketService.checkout_basket()

    return redirect(url_for('getBasketDetail'))

@app.route('/api/basket/<int:basketid>', methods=['GET'])
@auth_required()
@inject
def getBasketFromApi(basketservice: BasketService, basketid: int):
    return jsonify([item.get_json_parsable() for item in basketservice.find_one(basketid).items])