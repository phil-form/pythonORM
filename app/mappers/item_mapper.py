from app.dtos.item_dto import ItemDTO
from app.forms.item.item_add_form import ItemAddForm
from app.mappers.abstract_mapper import AbstractMapper
from app.models.item import Item


class ItemMapper(AbstractMapper):
    @staticmethod
    def entity_to_dto(item: Item):
        ItemDTO.build_from_entity(item)

    @staticmethod
    def form_to_entity(form, item: Item):
        if isinstance(form, ItemAddForm):
            item.itemname = form.itemname.data
            item.itemdescription = form.itemdescription.data
            item.itemstock = form.itemstock.data
        return item
