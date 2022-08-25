from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange, Length


class ItemForm(FlaskForm):
    itemname = StringField('itemname', validators=[DataRequired(), Length(min=2, max=255)])
    itemdescription = StringField('itemdescription', validators=[DataRequired()])
    itemstock = IntegerField('itemstock', validators=[DataRequired(), NumberRange(min=0)])