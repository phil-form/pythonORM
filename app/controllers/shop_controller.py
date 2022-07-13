from flask import render_template

from app import app
from app.services.item_service import ItemService

itemService = ItemService()


@app.route('/shop')
def getItemList():
    return render_template('items/list.html', items=itemService.find_all())
