from flask import render_template
from app import app
from app.services.item_service import ItemService

service = ItemService()

@app.route('/shop', methods=['GET'])
def shop():
    items = service.find_all()
    print(items)
    return render_template('item/shop.html', items=items)