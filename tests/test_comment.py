import unittest
from app.models import Comment

class CommentModelTest(unittest.TestCase):
   """
   test class to test the behavior of the  Comment class
   """
   def setUp(self):
      self.new_comment = Comment("1","josphat","josphatmax@gmail.com", "1234", "yudbc", "this is a great article") #create comment object
   
      