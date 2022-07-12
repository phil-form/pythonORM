from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import DataRequired, EqualTo
from app.models.user import User

class UserLoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    userpassword = StringField('userpassword', validators=[DataRequired()])

    def getAsUser(self) -> User:
        user = User()
        user.username = self.username.data
        user.userpassword = self.userpassword.data

        return user