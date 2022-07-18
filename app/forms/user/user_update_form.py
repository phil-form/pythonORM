from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, BooleanField, SelectMultipleField
from wtforms.validators import DataRequired, EqualTo
from app.models.user import User
from app.services.role_service import RoleService


class UserUpdateForm(FlaskForm):
    useremail = StringField('useremail', validators=[DataRequired()])
    userdescription = StringField('userdescription', validators=[DataRequired()])
    userroles = SelectMultipleField('userroles')

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.roleService = RoleService()
        self.userroles.choices = [str(role.roleid) for role in self.roleService.find_all_entities()]

    def manage_roles(self, user):
        for roleid in self.userroles.data:
            role = self.roleService.find_one_entity(int(roleid))
            user.tmp_roles.append(role)
