import unittest

from app.models import User, Post

class ProjectTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username='kiprotich', email='kiprotich@gmail.com', password='hdhdhdhs')
        self.new_post = Post()
        

if __name__ == '__main__':
    unittest.main()