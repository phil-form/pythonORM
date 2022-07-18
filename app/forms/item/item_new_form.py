from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Regexp
from app.models.item import Item

class ItemNewForm(FlaskForm):
    itemname        = StringField ('itemname'       , validators=[DataRequired()])
    itemdescription = StringField ('itemdescription', validators=[DataRequired()])
    itemstock       = IntegerField('itemstock'                                   )
