from app.models.item import Item

class ItemDTO:
    def __init__(self, itemid, itemname, itemprice):
        self.itemid = itemid
        self.itemname = itemname
        self.itemprice = itemprice

    @staticmethod
    def build_from_entity(item: Item):
        return ItemDTO(item.itemid, item.itemname, item.itemprice)