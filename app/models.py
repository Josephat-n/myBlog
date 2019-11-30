from . import db

class User(db.Model):
   __tablename__ = 'users'

   id = db.Column(db.Integer,primary_key = True)
   username = db.Column(db.String(255),index = True)
   email = db.Column(db.String(255),unique = True,index = True)
   pass_secure = db.Column(db.String(255))
   password_hash = db.Column(db.String(255))
   blogs = db.relationship('Blog',backref = 'user',lazy="dynamic")
   
   def __repr__(self):
      return f'User {self.username}'
   
class Blog(db.Model):
   __tablename__ = 'blogs'
   
   id = db.Column(db.Integer,primary_key = True)    
   blog_msg =  db.Column(db.String(2000))
   user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
   
   
   def __repr__(self):

      return f'Pitch {self.pitch_msg}'

