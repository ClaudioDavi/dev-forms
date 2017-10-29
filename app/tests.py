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

    def test_is_allowed(self):
        self.assertTrue(ctrl.is_allowed(7,8,9))
        self.assertTrue(ctrl.is_allowed(9,10,7))

    def test_is_not_allowed(self):
        self.assertFalse(ctrl.is_allowed(9, 10, 6))
        self.assertFalse(ctrl.is_allowed(0, 4, 8))
        self.assertFalse(ctrl.is_allowed(9, -2, 4))

if __name__ == "__main__":
    unittest.main()
