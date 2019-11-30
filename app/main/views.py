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

@main.route('/blog/<int:id>')
def blog(id):
   """
   Allow for commenting of a given blog.
   """
   #Should return a blog by id   
   a_blog = Blog.query.filter_by(id= id)
   print(a_blog)
   
   return render_template('blog.html', id = id, a_blog = a_blog)