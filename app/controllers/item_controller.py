from flask import render_template, request, redirect, url_for, jsonify
from app import app
from app.framework.decorators.inject import inject
from app.forms.basket.basket_add_item_form import BasketAddItemForm
from app.forms.item.item_form import ItemForm
from app.services.item_service import ItemService

itemService = ItemService()

@app.route('/items')
def getItemList():
    return render_template('items/list.html', items=itemService.find_all())

@app.route('/api/items')
@inject
def getItemsAsJson(item_service: ItemService):
    return jsonify([item.get_json_parsable() for item in item_service.find_all()])

@app.route('/items/<int:itemid>')
def getItemDetails(itemid):
    form = BasketAddItemForm()

    return render_template('items/details.html', item=itemService.find_one(itemid), form=form)

@app.route('/items/add', methods=['GET','POST'])
def addItem():
    form = ItemForm(request.form)

    if request.method == 'POST':
        if form.validate():
            item = itemService.insert(form)

            return redirect(url_for('getItemList'))

    print(form.errors)
    form.itemname.data = ''
    form.itemdescription.data = ''
    form.itemstock.data = 1

    return render_template('items/add_or_update.html', form=form)

@app.route('/items/update/<int:itemid>', methods=['GET','POST'])
def updateItem(itemid: int):
    item = itemService.find_one(itemid)

    if item is None:
        return redirect(url_for('getItemList'))

    form = ItemForm(request.form)

    if request.method == 'POST':
        if form.validate():
            item = itemService.update(itemid, form)

            return redirect(url_for('getItemList'))

    print(form.errors)
    form.itemname.data = item.itemname
    form.itemdescription.data = item.itemdescription
    form.itemstock.data = item.itemquantity

    return render_template('items/add_or_update.html', form=form)
