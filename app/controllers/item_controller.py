from flask import render_template, request, redirect, url_for

from app import app
from app.forms.item.item_add_form import ItemAddForm
from app.services.item_service import ItemService

itemService = ItemService()


@app.route('/items')
def getItemList():
    return render_template('items/list.html', items=itemService.find_all())


@app.route('/items/<int:itemid>')
def getItemDetails(itemid):
    return render_template('items/details.html', item=itemService.find_one(itemid))


@app.route('/items/add', methods=["GET", "POST"])
def addItem():
    form = ItemAddForm(request.form)

    if request.method == 'POST':
        if form.validate():
            item = itemService.insert(form)

            return redirect(url_for('getItemDetails', itemid=item.itemid))

    return render_template('items/add.html', form=form)
