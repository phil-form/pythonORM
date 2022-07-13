from app.models.item import Item


class ItemDTO:
    def __init__(self, itemid, itemname, itemdescription, quantity):
        self.itemid = itemid
        self.itemname = itemname
        self.itemdescription = itemdescription
        self.quantity = quantity

    @staticmethod
    def build_from_entity(item: Item):
        return ItemDTO(item.itemid, item.itemname, item.itemdescription)
