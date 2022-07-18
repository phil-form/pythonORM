from flask import session

from app import db
from app.forms.user.user_login_form import UserLoginForm
from app.forms.user.user_register_form import UserRegisterForm
from app.forms.user.user_update_form import UserUpdateForm
from app.models.role import Role
from app.models.user import User
from app.services.base_service import BaseService
from app.mappers.user_mapper import UserMapper
import bcrypt


class UserService(BaseService):
    def find_all(self):
        return [UserMapper.entity_to_dto(user) for user in User.query.filter_by(active=True).all()]

    def find_one(self, entity_id: int):
        return UserMapper.entity_to_dto(User.query.filter_by(userid=entity_id).first())

    def find_one_by(self, **kwargs) -> User:
        return User.query.filter_by(**kwargs).first()

    def insert(self, form: UserRegisterForm):
        user = User()
        UserMapper.form_to_entity(form, user)
        password = user.userpassword.encode('utf-8')
        salt = bcrypt.gensalt()
        user.userpassword = bcrypt.hashpw(password, salt).decode('utf-8')

        role_user = Role.query.filter_by(rolename="USER").one()
        user.add_role(role_user)

        try:
            db.session.add(user)
            db.session.commit()
        except:
            db.session.rollback()

        return self.find_one(user.userid)

    def update(self, entity_id: int, form: UserUpdateForm):
        user = User.query.filter_by(userid=entity_id).first()
        UserMapper.form_to_entity(form, user)

        if user.tmp_roles is not [] and "ADMIN" in session.get('userroles'):
            for role in user.tmp_roles:
                user.add_role(role)
            for role in [r.rel_role for r in user.roles]:
                if role.rolename not in [r.rolename for r in user.tmp_roles]:
                    user.remove_role(role)
            if session.get('userid') == user.userid:
                session['userroles'] = user.get_roles()

        try:
            db.session.commit()
        except:
            db.session.rollback()
            return None

        return UserMapper.entity_to_dto(user)

    def delete(self, entity_id: int):
        user = User.query.filter_by(userid=entity_id).first()

        if user is not None:
            db.session.delete(user)
            db.session.commit()

        return user.userid

    def login(self, form: UserLoginForm):
        user = User()
        UserMapper.form_to_entity(form, user)
        to_login = self.find_one_by(username=user.username)

        if to_login is not None and bcrypt.checkpw(user.userpassword.encode('utf-8'), to_login.userpassword.encode('utf-8')):
            return to_login

        return None