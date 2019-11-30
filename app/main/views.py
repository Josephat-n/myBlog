from flask import render_template
from . import main
from .. import db
from ..models import Blog


@main.route('/')
def index():   
   """Fetch the blogs from the database"""   
   blogs = Blog.query.all()
   print(blogs)
   return render_template('index.html', blogs = blogs)