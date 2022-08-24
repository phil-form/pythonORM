from app import app
from app.forms.item.item_form import ItemForm
from app.framework.decorators.auth_required import auth_required
from app.framework.decorators.inject import inject
from app.services.item_service import ItemService
from flask import jsonify, redirect, render_template, request, url_for


@app.route("/api/items")
@inject
def getItemListAsJson(itemService: ItemService):
    return jsonify([item.get_json_parsable() for item in itemService.find_all()])


@app.route("/api/items/<int:itemid>")
@inject
def getItemDetails(itemid, itemService: ItemService):
    return jsonify(itemService.find_one(itemid).get_json_parsable())


@app.route("/api/items/add", methods=["POST"])
@auth_required(level="ADMIN")
@inject
def addItem(itemService: ItemService):
    form = ItemForm.from_json(request.json)

    if form.validate():
        item = itemService.insert(form)

        return jsonify(item.get_json_parsable())

    form.itemname.data = ""
    form.itemdescription.data = ""
    form.itemstock.data = 1

    return jsonify(form.errors)


@app.route("/api/items/<int:itemid>", methods=["PUT"])
@auth_required(level="ADMIN")
@inject
def updateItem(itemid: int, itemService: ItemService):
    item = itemService.find_one(itemid)

    if item is None:
        return jsonify({"errors": "item not found"})

    form = ItemForm(request.form)

    if form.validate():
        item = itemService.update(itemid, form)

        return jsonify(item.get_json_parsable())

    return jsonify(form.errors)
