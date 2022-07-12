from app import db
from app.models.base_entity import BaseEntity
from app.models.role import Role
from app.models.user_role import UserRole


class User(db.Model, BaseEntity):
    __tablename__ = "users"
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    useremail = db.Column(db.String(100), unique=True, nullable=False, index=True)
    userpassword = db.Column(db.String(100), nullable=False)
    userdescription = db.Column(db.String(255), nullable=False)
    roles = db.relationship('UserRole')

    def add_role(self, role: Role):
        if role.rolename in self.get_roles():
            return
        
        userrole = UserRole()
        userrole.rel_role = role
        userrole.rel_user = self
        self.roles.append(userrole)

    def remove_role(self, role: Role):
        userrole: UserRole
        for userrole in self.roles:
            if userrole.roleid == role.roleid:
                self.roles.remove(userrole)
                break

    def get_roles(self):
        return [role.rel_role.rolename for role in self.roles]
