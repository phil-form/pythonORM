from flask import render_template

from app import app
from app.services.item_service import ItemService

itemService = ItemService

@app.route('/items')
def getItemList():
    return render_template('items/list.html', items=itemService.find_all())

@app.route('/items/<int:itemid>')
def getItemDetails(itemid):
    return render_template('items/details.html', item=itemService.find_one(itemid))