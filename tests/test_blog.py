import unittest
from app.models import Blog

class BlogModelTest(unittest.TestCase):
   """
   test class to test the behavior of the  Blog class
   """
   def setUp(self):
      self.new_blog = Blog("1","The BBI is no deifferent from the other reports that we have had. We should first ask more definate questions like where is our country headed?","1") #create a blog object
   
      