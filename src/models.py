import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    birth_date = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"))
    user_post = relationship("posts", backref = "Users")

class Posts(Base):
    __tablename__ = 'posts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_name = Column(String(250))
    location_id = Column(Integer, ForeignKey("locations.id"))
    post_location = relationship("locations", backref = "Posts")
    category_id = Column(Integer, ForeignKey("categories.id"))
    post_category = relationship("categories", backref = "Posts")
    hashtag_id = Column(Integer, ForeignKey('hashtags.id'))
    post_hashtag = relationship("hashtags", backref = "Posts")
    collection_id = Column(Integer, ForeignKey('collections.id'))
    post_collection = relationship("collections", backref = "Posts")

class Locations(Base):
    __tablename__ = 'locations'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    location_name = Column(String(250))

class Categories(Base):
    __tablename__ = 'categories'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    category_name = Column(String(250))

class Hashtags(Base):
    __tablename__ = 'hashtags'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    hashtag_name = Column(String(250))

class Collections(Base):
    __tablename__ = 'collections'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    category_name = Column(String(250))
    post_id = Column(Integer, ForeignKey("posts.id"))
    user_post = relationship(Posts)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e