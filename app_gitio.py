# https://stevenloria.com/hosting-static-flask-sites-on-github-pages/

import sys, os
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_flatpages import FlatPages
from flask_frozen import Freezer

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# set up the SQLAlchemy database and store the content locally
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_pyfile('settings.py')
pages = FlatPages(app)
freezer = Freezer(app)

# initialize a db object that represents the database, passing in app as the parameter
db = SQLAlchemy(app)

if __name__ == '__main__':

  # need to import views
  from views import*
  app.secret_key = os.urandom(12)
  app.run(debug=True)
