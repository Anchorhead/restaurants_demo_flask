from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import Required

class NewRestaurantForm(FlaskForm):
    name = StringField('Enter name for new restaurant', validators=[Required()])
    submit = SubmitField('Create')

class EditRestaurantForm(FlaskForm):
    name = StringField('Enter desired name', validators=[Required()])
    submit = SubmitField('Edit')

class DeleteRestaurantForm(FlaskForm):
    submit = SubmitField('Delete')

class NewMenuItemForm(FlaskForm):
    name = StringField('Enter name for new menu item', validators=[Required()])
    description = StringField('Enter description for new menu item', validators=[Required()])
    price = DecimalField('Enter price for new menu item', validators=[Required()])
    submit = SubmitField('Create')

class EditMenuItemForm(FlaskForm):
    name = StringField('Enter desired name')
    description = StringField('Enter new description')
    price = DecimalField('Enter new price')
    submit = SubmitField('Edit')

class DeleteMenuItemForm(FlaskForm):
    submit = SubmitField('Delete')
