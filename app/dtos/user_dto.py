from app.dtos.abstract_dto import AbstractDTO
from app.models.user import User
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

    @staticmethod
    def build_from_entity(user: User):
        user_dto = UserDTO()

        user_dto.userid = user.userid
        user_dto.username = user.username
        user_dto.useremail = user.useremail
        user_dto.userdescription = user.userdescription
        user_dto.userroles = []
        for role in user.roles:
            user_dto.userroles.append(RoleDTO(role.rel_role.roleid, role.rel_role.rolename))

    def get_json(self):
        pass
