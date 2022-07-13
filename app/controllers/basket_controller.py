from app.services.basket_service import BasketService
from app import app
from flask import render_template

basketService = BasketService()

@app.route('/baskets')
def getBasketList():
    return render_template('baskets/list.html', baskets=basketService.find_all())

@app.route('/baskets/<int:basketid>', methods=["GET"])
def getOneBasket(basketid: int):
    basket = basketService.find_one(basketid)

    return render_template('baskets/one.html', basket=basket)