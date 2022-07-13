from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import DataRequired, EqualTo, Regexp
from app.models.user import User

class UserRegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    userpassword = StringField('userpassword', validators=[DataRequired(), EqualTo('confirm', message='passwords must match!')])
    confirm = StringField('confirm', validators=[DataRequired()])
    useremail = StringField('useremail', validators=[DataRequired()])
    userdescription = StringField('userdescription', validators=[DataRequired()])