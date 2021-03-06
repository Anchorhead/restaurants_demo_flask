import os
import sys
from sqlalchemy import Column, ForeignKey, String, Integer, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    restaurant_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Menu_Item(Base):
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key=True)
    item_name = Column(String(250), nullable=False)
    item_description = Column(String(250), nullable=False)
    item_price = Column(Numeric, nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurants.restaurant_id'))
    restaurant = relationship(Restaurant)
