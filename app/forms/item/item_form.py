from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class ItemForm(FlaskForm):
    itemname = StringField('itemname', validators=[DataRequired()])
    itemdescription = StringField('itemdescription', validators=[DataRequired()])
    itemstock = IntegerField('itemstock', validators=[DataRequired(), NumberRange(min=0)])