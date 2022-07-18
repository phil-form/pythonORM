from app.dtos.role_dto import RoleDTO
from app.models.role import Role
from app.services.base_service import BaseService


class RoleService(BaseService):
    def find_all(self):
        return [RoleDTO.build_from_entity(role) for role in Role.query.all()]

    def find_all_entities(self):
        return Role.query.all()

    def find_one(self, entity_id: int):
        pass

    def find_one_entity(self, entity_id: int):
        return Role.query.filter_by(roleid=entity_id).one()

    def find_one_by(self, **kwargs):
        pass

    def insert(self, data):
        pass

    def update(self, entity_id: int, data):
        pass

    def delete(self, entity_id: int):
        pass