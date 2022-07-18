from app.dtos.abstract_dto import AbstractDTO
from app.models.role import Role


class RoleDTO(AbstractDTO):
    def __init__(self):
        self.roleid = None
        self.rolename = None

    @staticmethod
    def build_from_entity(entity: Role):
        role_dto = RoleDTO()

        role_dto.roleid = entity.roleid
        role_dto.rolename = entity.rolename

        return role_dto

    def get_json_parsable(self):
        pass

