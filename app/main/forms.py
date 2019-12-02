from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class CommentForm(FlaskForm):
  comment = TextAreaField('Your Comment',validators=[Required()])
  submit = SubmitField('Submit')
 
class BlogForm(FlaskForm):
  title = StringField('Blog title',validators=[Required()])
  blog_msg = TextAreaField('Blog message')
  submit = SubmitField('Submit')