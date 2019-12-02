from flask import render_template, redirect, url_for
from . import main
from .. import db
from ..models import Blog, User
from .forms import CommentForm, BlogForm, UpdateProfile
from flask_login import login_user,login_required,current_user,logout_user


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

@main.route('/blog/')
def blog():
   """
   path for creating a new blog
   """
   return render_template('blog.html')

@main.route('/user/<uname>')
def profile(uname):
   user = User.query.filter_by(username = uname).first()

   if user is None:
      abort(404)

   return render_template("profile/profile.html", user = user)
   
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
 
