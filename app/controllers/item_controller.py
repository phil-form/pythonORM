from flask import render_template, request, redirect, url_for, jsonify
<<<<<<< HEAD
from app.framework.decorators.inject import inject
=======

>>>>>>> ba4c094cc8ebdde3a1fada1b67d21c58f15f8067
from app import app
from app.forms.basket.basket_add_item_form import BasketAddItemForm
from app.forms.item.item_form import ItemForm
from app.framework.decorators.inject import inject
from app.services.item_service import ItemService

@app.route('/items')
<<<<<<< HEAD
@inject
def getItemList(item_service: ItemService):
    form = ItemForm()
    return render_template('items/list.html', items=item_service.find_all(), form=form)

@app.route('/api/items')
@inject
def getItemsAsJson(item_service: ItemService):
    return jsonify([item.get_json_parsable() for item in item_service.find_all()])
=======
def getItemList():
    form = ItemForm();
    return render_template('items/list.html', items=itemService.find_all(), form=form)

@app.route('/api/items')
@inject
def getItemListAsJson(itemService: ItemService):
    return jsonify([item.get_json_parsable() for item in itemService.find_all()])
>>>>>>> ba4c094cc8ebdde3a1fada1b67d21c58f15f8067

@app.route('/items/<int:itemid>')
@inject
def getItemDetails(itemid, item_service: ItemService):
    form = BasketAddItemForm()

    return render_template('items/details.html', item=item_service.find_one(itemid), form=form)

@app.route('/items/add', methods=['GET','POST'])
@inject
def addItem(item_service: ItemService):
    form = ItemForm(request.form)

    if request.method == 'POST':
        if form.validate():
            item = item_service.insert(form)

            return redirect(url_for('getItemList'))

    print(form.errors)
    form.itemname.data = ''
    form.itemdescription.data = ''
    form.itemstock.data = 1

    return render_template('items/add_or_update.html', form=form)

@app.route('/items/update/<int:itemid>', methods=['GET','POST'])
@inject
def updateItem(itemid: int, item_service: ItemService):
    item = item_service.find_one(itemid)

    if item is None:
        return redirect(url_for('getItemList'))

    form = ItemForm(request.form)

    if request.method == 'POST':
        if form.validate():
            item = item_service.update(itemid, form)

            return redirect(url_for('getItemList'))

    print(form.errors)
    form.itemname.data = item.itemname
    form.itemdescription.data = item.itemdescription
    form.itemstock.data = item.itemquantity

    return render_template('items/add_or_update.html', form=form)
