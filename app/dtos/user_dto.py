from app.models.user import User
from app.dtos.role_dto import RoleDTO


class UserDTO:
    def __init__(self, userid, username, useremail, userdescription, roles):
        self.userid = userid
        self.username = username
        self.useremail = useremail
        self.userdescription = userdescription
        self.userroles = []
        for role in roles:
            self.userroles.append(RoleDTO(role.rel_role.roleid, role.rel_role.rolename).__dict__)

    def is_admin(self):
        return "ADMIN" in self.userroles

    @staticmethod
    def build_from_entity(user: User):
        return UserDTO(user.userid, user.username, user.useremail, user.userdescription, user.roles)
