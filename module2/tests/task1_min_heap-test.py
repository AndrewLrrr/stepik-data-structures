import unittest

from module2.task1_min_heap import MinHeap


class TestMinHeap(unittest.TestCase):
    def test1(self):
        h = MinHeap([5, 4, 3, 2, 1])
        self.assertEquals([(1, 4), (0, 1), (1, 3)], h.log())
        self.assertEqual(1, h.extract_min())
        self.assertEqual(2, h.extract_min())

    def test2(self):
        h = MinHeap([1, 2, 3, 4, 5])
        self.assertEquals([], h.log())
        self.assertEqual(1, h.extract_min())
        self.assertEqual(2, h.extract_min())

    def test3(self):
        h = MinHeap([7, 6, 5, 4, 3, 2])
        self.assertEquals([(2, 5), (1, 4), (0, 2), (2, 5)], h.log())
        self.assertEqual(2, h.extract_min())
        h.insert(1)
        self.assertEqual(1, h.extract_min())
        h.insert(4)
        self.assertEqual(3, h.extract_min())
        self.assertEqual(4, h.extract_min())
        self.assertEqual(4, h.extract_min())
