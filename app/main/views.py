from flask import render_template, redirect, url_for
from . import main
from .. import db
from ..models import Blog
from .forms import CommentForm


@main.route('/')
def index():   
   """Fetch the blogs from the database"""   
   blogs = Blog.query.all()
   print(blogs)
   return render_template('index.html', blogs = blogs)

@main.route('/comment/<int:id>')
def comment(id):
   """
   Allow for commenting of a given blog.
   """
   #Should return a blog by id   
   a_blog = Blog.query.filter_by(id= id)
   print(a_blog)
   form = CommentForm()
   
   return render_template('comment.html',a_blog = a_blog, comment_form=form)