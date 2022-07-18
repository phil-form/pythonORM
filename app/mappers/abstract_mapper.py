from abc import ABC, abstractmethod


class AbstractMapper(ABC):
    @abstractmethod
    def entity_to_dto(entity):
        pass

    @abstractmethod
    def form_to_entity(form, entity):
        pass