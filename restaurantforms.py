from flask_wtf import Form
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import Required

class NewRestaurantForm(Form):
    name = StringField('Enter name for new restaurant', validators=[Required()])
    submit = SubmitField('Create')

class EditRestaurantForm(Form):
    name = StringField('Enter desired name', validators=[Required()])
    submit = SubmitField('Edit')

class DeleteRestaurantForm(Form):
    submit = SubmitField('Delete')

class NewMenuItemForm(Form):
    name = StringField('Enter name for new menu item', validators=[Required()])
    description = StringField('Enter description for new menu item', validators=[Required()])
    price = DecimalField('Enter price for new menu item', validators=[Required()])
    submit = SubmitField('Create')

class EditMenuItemForm(Form):
    name = StringField('Enter desired name')
    description = StringField('Enter new description')
    price = DecimalField('Enter new price')
    submit = SubmitField('Edit')

class DeleteMenuItemForm(Form):
    submit = SubmitField('Delete')
