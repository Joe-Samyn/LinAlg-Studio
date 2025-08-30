import unittest
from sols import Vector2

class TestVector2(unittest.TestCase):

    def test_createVector2(self):
        # arrange

        # act
        vector = Vector2(2, 3)

        # assert
        self.assertEqual(vector, Vector2(2, 3))

    def test_createZeroVector(self):
        pass