from flask import render_template, session, request, redirect, url_for, jsonify

from app import app
from app.framework.decorators.auth_required import auth_required
from app.forms.basket.basket_add_item_form import BasketAddItemForm
from app.framework.decorators.inject import inject
from app.services.auth_service import AuthService
from app.services.basket_service import BasketService

@app.route('/api/basket/all')
@auth_required(level="ADMIN")
@inject
def getAllBaskets(basketService: BasketService):
    return jsonify([basket.get_json_parsable() for basket in basketService.find_all()])

@app.route('/api/basket')
@auth_required()
@inject
def getBasketDetail(basketService: BasketService, authService: AuthService):
    user = authService.get_current_user()
    basket = basketService.find_one_by(userid=user.userid, basketclosed=False)
    return jsonify(basket.get_json_parsable())

@app.route('/api/basket/', methods=['PUT'])
@auth_required()
@inject
def add_item_to_basket(basketService: BasketService):
    item_to_add = BasketAddItemForm.from_json(request.json)

    basket = basketService.add_item(item_to_add)

    return jsonify({ 'status': 'added' })

@app.route('/api/basket/<int:itemid>', methods=['DELETE'])
@auth_required()
@inject
def remove_item_to_basket(itemid: int, basketService: BasketService):
    basketService.remove_item(itemid)

    return jsonify({ 'status': 'removed' })

@app.route('/api/basket/checkout', methods=['POST'])
@auth_required()
@inject
def checkout_basket(basketService: BasketService):
    basketService.checkout_basket()

    return jsonify({ 'status': 'checkout' })