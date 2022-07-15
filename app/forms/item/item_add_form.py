from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import DataRequired, EqualTo, Regexp
from app.models.item import Item

class ItemAddForm(FlaskForm):
    itemname = StringField('username', validators=[DataRequired()])
    itemdescription = StringField('userdescription', validators=[DataRequired()])