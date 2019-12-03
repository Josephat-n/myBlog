import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
   """
   test class to test the behavior of the  User class
   """
   def setUp(self):
      self.new_user = User("1","josphat","josphatmax@gmail.com", "1234", "yudbc", "this is a great article") #create a user object
   
   def test_setting_password(self):
       '''
    testcase to test on setting a new password
    '''
    self.assertFalse(self.new_user.pass_secure is None)

  def test_no_access_to_passwd(self):
    '''
    testcase to test that no can access a password from the database
    '''
    if self.new_user.pass_secure:
      return self.assertRaises(AttributeError)

    else:
      return self.assertRaises('False')  

  def test_password_verify(self):
    '''
    testcase to check verifying of hashed password  to login a user
    '''
    self.assertTrue(self.new_user.verify_password,('1234'))    
   