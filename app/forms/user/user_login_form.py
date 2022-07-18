from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import DataRequired, EqualTo
from app.models.user import User

class UserLoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    userpassword = StringField('userpassword', validators=[DataRequired()])