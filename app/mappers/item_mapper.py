<<<<<<< HEAD
from app.models.item import Item
from app.dtos.item_dto import ItemDTO

class ItemMapper:
    def entity_to_dto(entity: Item):
        return ItemDTO.build_from_entity(entity)
=======
from app.dtos.item_dto import ItemDTO
from app.forms.item.item_form import ItemForm
from app.mappers.abstract_mapper import AbstractMapper
from app.models.item import Item


class ItemMapper(AbstractMapper):
    @staticmethod
    def entity_to_dto(item: Item):
        return ItemDTO.build_from_entity(item)

    @staticmethod
    def form_to_entity(form, item: Item):
        if isinstance(form, ItemForm):
            item.itemname = form.itemname.data
            item.itemdescription = form.itemdescription.data
            item.itemstock = form.itemstock.data

        return item
>>>>>>> main
