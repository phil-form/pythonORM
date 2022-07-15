from flask import render_template, session, request

from app import app
from app.decorators.auth_required import auth_required
from app.services.basket_service import BasketService

basketService = BasketService()


@app.route('/basket/all')
@auth_required(level="ADMIN")
def getAllBaskets():
    return render_template('baskets/list.html', baskets=basketService.find_all())


@app.route('/basket', methods=['GET', 'POST'])
@auth_required()
def getBasketDetail():
    print(request.method)
    userid = session.get('userid')
    basket = basketService.find_one_by(userid=userid)
    if request.method == 'POST':
        print("here")
        itemid = int(request.args.get('itemid'))
        itemqty = request.form['itemquantity']
        basket = basketService.addToBasket(basket.basketid, itemid, itemqty)

    return render_template('baskets/details.html',
                           basket=basket, items=basket.items, is_basket=True)
