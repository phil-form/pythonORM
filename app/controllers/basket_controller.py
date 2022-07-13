from flask import render_template

from app import app
from app.services.basket_service import BasketService

basketService = BasketService()


@app.route('/users/<int:userid>/basket', methods=["GET"])
def getBasketUser(userid: int):
    basket = basketService.find_one_by(userid=userid)
    return render_template('baskets/user_basket.html', items=basket.items)
