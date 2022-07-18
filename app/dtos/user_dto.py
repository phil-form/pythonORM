from app.dtos.abstract_dto import AbstractDTO
from app.dtos.role_dto import RoleDTO


class UserDTO(AbstractDTO):
    def __init__(self):
        self.userid = None
        self.username = None
        self.useremail = None
        self.userdescription = None
        self.userroles = []

    def is_admin(self):
        return "ADMIN" in self.userroles

    def get_roles(self):
        return [role.rolename for role in self.userroles]

    @staticmethod
    def build_from_entity(user):
        user_dto = UserDTO()

        user_dto.userid = user.userid
        user_dto.username = user.username
        user_dto.useremail = user.useremail
        user_dto.userdescription = user.userdescription
        user_dto.userroles = []
        for role in user.roles:
            user_dto.userroles.append(RoleDTO.build_from_entity(role.rel_role))

        return user_dto

    def get_json_parsable(self):
        return self.__dict__
