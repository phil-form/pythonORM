from abc import ABC, abstractmethod


class AbstractDTO(ABC):
    @abstractmethod
    def build_from_entity(entity):
        pass

    @abstractmethod
    def get_json_parsable(self):
        pass