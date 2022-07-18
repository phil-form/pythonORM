from app import db
from app.models.base_entity import BaseEntity

class UserRole(BaseEntity, db.Model):
    __tablename__ = "userroles"
    userid = db.Column(db.ForeignKey("users.userid"), primary_key=True)
    roleid = db.Column(db.ForeignKey("roles.roleid"), primary_key=True)

    rel_user = db.relationship('User', back_populates="roles")
    rel_role = db.relationship('Role', back_populates="users")