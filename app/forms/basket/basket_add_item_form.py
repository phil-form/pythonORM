from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired


class BasketAddItemForm(FlaskForm):
    itemid = IntegerField('itemid', validators=[DataRequired()])
    itemquantity = IntegerField('itemquantity', validators=[DataRequired()])