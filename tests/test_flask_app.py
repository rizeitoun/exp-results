import unittest
from exp_results import app


class TestStringMethods(unittest.TestCase):

    def test_message(self):
        self.assertEqual(app.home(), 'Hello, World!')
