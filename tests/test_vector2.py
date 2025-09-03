import unittest
from linalg import Vector2

class TestVector2(unittest.TestCase):

    def test_createVector2(self):
        # arrange

        # act
        vector = Vector2(2, 3)

        # assert
        self.assertEqual(vector, Vector2(2, 3))

    def test_createZeroVector(self):
        # arrange
        exp = Vector2(0, 0)

        # act
        vector = Vector2.zero()

        # assert
        self.assertEqual(exp, vector)