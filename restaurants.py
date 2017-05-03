from os import environ
from flask import Flask, render_template, request, url_for, redirect
from flask_wtf  import FlaskForm
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbsetup import Base, Restaurant, Menu_Item

from restaurantforms import NewRestaurantForm, EditRestaurantForm, DeleteRestaurantForm, NewMenuItemForm, EditMenuItemForm, DeleteMenuItemForm

app = Flask(__name__)
app.secret_key = environ['SECRET_KEY']
Bootstrap(app)
csrf = CSRFProtect()
csrf.init_app(app)

engine = create_engine(environ['DATABASE_URL'])
DBSession = sessionmaker(bind=engine)

@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    session = DBSession()
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants = restaurants)

@app.route('/restaurants/new/', methods=['GET', 'POST'])
def restaurantsNew():
    session = DBSession()
    form = NewRestaurantForm()
    if request.method == 'POST' and form.validate():
        newRestaurant = Restaurant(name=form.name.data)
        session.add(newRestaurant)
        session.commit()
        return redirect(url_for('showRestaurants'))
    return render_template('newrestaurant.html', form = form)

@app.route('/restaurants/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def restaurantsEdit(restaurant_id):
    session = DBSession()
    form = EditRestaurantForm()
    restaurant = session.query(Restaurant).filter_by(restaurant_id=restaurant_id).one()
    if request.method == 'POST' and form.validate():
        restaurant.name = form.name.data
        session.add(restaurant)
        session.commit()
        return redirect(url_for('showRestaurants'))
    return render_template('editrestaurant.html', restaurant = restaurant, form = form)

@app.route('/restaurants/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def restaurantsDelete(restaurant_id):
    session = DBSession()
    form = DeleteRestaurantForm()
    restaurant = session.query(Restaurant).filter_by(restaurant_id=restaurant_id).one()
    items = session.query(Menu_Item).filter_by(restaurant_id=restaurant_id).all()
    if request.method == 'POST' and form.validate():
        if form.submit.data:
            session.delete(restaurant)
            if items:
                for i in items:
                    session.delete(i)
            session.commit()
        return redirect(url_for('showRestaurants'))
    return render_template('deleterestaurant.html', restaurant = restaurant, form = form)

@app.route('/restaurants/<int:restaurant_id>/menu/')
def restaurantsMenu(restaurant_id):
    session = DBSession()
    restaurant = session.query(Restaurant).filter_by(restaurant_id=restaurant_id).one()
    items = session.query(Menu_Item).filter_by(restaurant_id=restaurant_id).all()
    session.commit()
    return render_template('menu.html', restaurant = restaurant, items = items)

@app.route('/restaurants/<int:restaurant_id>/menu/new/', methods=['GET', 'POST'])
def restaurantsMenuItemNew(restaurant_id):
    session = DBSession()
    form = NewMenuItemForm()
    restaurant = session.query(Restaurant).filter_by(restaurant_id=restaurant_id).one()
    if request.method == 'POST' and form.validate():
        items = session.query(Menu_Item).filter_by(restaurant_id=restaurant_id).all()
        newMenuItem = Menu_Item(item_name=form.name.data, item_description=form.description.data, item_price = form.price.data, restaurant_id=restaurant_id)
        session.add(newMenuItem)
        session.commit()
        return redirect(url_for('restaurantsMenu',  restaurant_id=restaurant_id))
    return render_template('newmenuitem.html', restaurant = restaurant, form = form)

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/', methods=['GET', 'POST'])
def restaurantsMenuEdit(restaurant_id, menu_id):
    session = DBSession()
    form = EditMenuItemForm()
    restaurant = session.query(Restaurant).filter_by(restaurant_id=restaurant_id).one()
    item = session.query(Menu_Item).filter_by(id=menu_id).one()
    if request.method == 'POST' and form.validate():
        if form.name.data:
            item.name = form.name.data
        if form.description.data:
            item.description = form.description.data
        if form.price.data:
            item.price = form.description.price
        session.add(item)
        session.commit()
        return redirect(url_for('restaurantsMenu', restaurant_id=restaurant_id))
    return render_template('editmenuitem.html', restaurant = restaurant, form = form, item = item)

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/', methods=['GET', 'POST'])
def restaurantsMenuDelete(restaurant_id, menu_id):
    session = DBSession()
    form = DeleteMenuItemForm()
    restaurant = session.query(Restaurant).filter_by(restaurant_id=restaurant_id).one()
    item = session.query(Menu_Item).filter_by(id=menu_id).one()
    if request.method == 'POST' and form.validate():
        if form.submit.data:
            session.delete(item)
            session.commit()
        return redirect(url_for('restaurantsMenu', restaurant_id=restaurant_id))
    return render_template('deletemenuitem.html', restaurant = restaurant, form = form, item = item)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
