from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class ItemAddForm(FlaskForm):
    itemname = StringField('username', validators=[DataRequired()])
    itemdescription = StringField('username', validators=[DataRequired()])
    itemstock = IntegerField('itemstock', validators=[DataRequired()])
