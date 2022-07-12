from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, BooleanField
from wtforms.validators import DataRequired, EqualTo
from app.models.user import User

class UserUpdateForm(FlaskForm):
    useremail = StringField('useremail', validators=[DataRequired()])
    userdescription = StringField('userdescription', validators=[DataRequired()])

    def getAsUser(self) -> User:
        user = User()
        user.useremail = self.useremail.data
        user.userdescription = self.userdescription.data

        return user