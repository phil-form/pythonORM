from abc import ABC, abstractmethod


class BaseService(ABC):
    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_one(self, entity_id: int):
        pass

    @abstractmethod
    def find_one_by(self, **kwargs):
        pass

    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def update(self, entity_id: int, data):
        pass

    @abstractmethod
    def delete(self, entity_id: int):
        pass