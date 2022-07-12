from app import db
from app.models.base_entity import BaseEntity

class User(db.Model, BaseEntity):
    __tablename__ = "users"
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    useremail = db.Column(db.String(100), unique=True, nullable=False, index=True)
    userpassword = db.Column(db.String(100), nullable=False)
    userdescription = db.Column(db.String(255), nullable=False)