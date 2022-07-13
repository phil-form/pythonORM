from flask import render_template, session

from app import app
from app.decorators.auth_required import auth_required
from app.services.basket_service import BasketService

basketService = BasketService

@app.route('/basket/all')
@auth_required(level="ADMIN")
def getAllBaskets():
    return render_template('baskets/list.html', baskets=basketService.find_all())

@app.route('/basket')
@auth_required()
def getBasketDetail():
    return render_template('baskets/details.html',
                           basket=basketService.find_one_by(userid=session.get('userid'), basketclosed=False))
