import unittest
import app.controllers as ctrl
from app import app, mail


class TestController(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        mail.init_app(app)
        self.assertEqual(app.debug, False)

    def tearDown(self):
        pass

    def test_should_return_front(self):
        self.assertTrue(ctrl.is_front(7, 7, 7))
        self.assertTrue(ctrl.is_front(8, 9, 10))

    def test_should_not_return_front(self):
        self.assertFalse(ctrl.is_front(6, 9, 9))
        self.assertFalse(ctrl.is_front(0, 2, 3))

    def test_should_return_back(self):
        self.assertTrue(ctrl.is_back(7, 7))
        self.assertTrue(ctrl.is_back(10, 10))

    def test_should_not_return_back(self):
        self.assertFalse(ctrl.is_back(5, 7))
        self.assertFalse(ctrl.is_back(9, 4))
        self.assertFalse(ctrl.is_back(2, 2))

    def test_should_return_mobile(self):
        self.assertTrue(ctrl.is_mobile(10, 7))
        self.assertTrue(ctrl.is_mobile(7, 7))

    def test_should_not_return_mobile(self):
        self.assertFalse(ctrl.is_mobile(6, 10))
        self.assertFalse(ctrl.is_mobile(10, 5))



if __name__ == "__main__":
    unittest.main()
