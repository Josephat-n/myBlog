import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
   """
   test class to test the behavior of the  User class
   """
   def setUp(self):
      self.new_user = User("1","josphat","josphatmax@gmail.com", "1234", "yudbc", "this is a great article") #create a user object
   
      