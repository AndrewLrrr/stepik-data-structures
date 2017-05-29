import unittest

from module1.task2_tree_height_decoder import tree_height_decoder


class TestTreeHeightDecoder(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, tree_height_decoder([4, -1, 4, 1, 1]))

    def test_2(self):
        self.assertEqual(4, tree_height_decoder([-1, 0, 4, 0, 3]))

    def test_3(self):
        self.assertEqual(4, tree_height_decoder([9, 7, 5, 5, 2, 9, 9, 9, 2, -1]))

    def test_4(self):
        self.assertEqual(1, tree_height_decoder([-1]))

    def test_5(self):
        self.assertEqual(2, tree_height_decoder([-1, 0, 0, 0]))

    def test_6(self):
        self.assertEqual(5, tree_height_decoder([-1, 0, 1, 2, 3]))

    def test_7(self):
        self.assertEqual(5, tree_height_decoder([3, 0, 1, -1, 2]))

    def test_8(self):
        self.assertEqual(5, tree_height_decoder([9, 7, 5, 5, 2, 9, 9, 9, 2, -1, 2, 10]))
