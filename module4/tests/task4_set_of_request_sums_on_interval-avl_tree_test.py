import unittest

from module4.task4_set_of_request_sums_on_interval import IntervalSet, AVLTree


class TestIntervalSet(unittest.TestCase):
    def test_tree_balance_after_add_and_remove(self):
        i_set = IntervalSet()
        i_set.add(12)
        i_set.add(5)
        node = i_set.add(4)
        self.assertEquals([{'key': 4, 'height': 1, 'sum': 4},
                           {'key': 5, 'height': 2, 'sum': 21},
                           {'key': 12, 'height': 1, 'sum': 12}], i_set.in_order(node))
        i_set.add(6)
        i_set.add(8)
        i_set.add(18)
        node = i_set.add(28)
        self.assertEquals([{'key': 4, 'sum': 4, 'height': 1},
                           {'key': 5, 'sum': 15, 'height': 2},
                           {'key': 6, 'sum': 6, 'height': 1},
                           {'key': 8, 'sum': 81, 'height': 3},
                           {'key': 12, 'sum': 12, 'height': 1},
                           {'key': 18, 'sum': 58, 'height': 2},
                           {'key': 28, 'sum': 28, 'height': 1}], i_set.in_order(node))
        node = i_set.add(30)
        self.assertEquals([{'height': 1, 'key': 4, 'sum': 4},
                           {'height': 2, 'key': 5, 'sum': 15},
                           {'height': 1, 'key': 6, 'sum': 6},
                           {'height': 4, 'key': 8, 'sum': 111},
                           {'height': 1, 'key': 12, 'sum': 12},
                           {'height': 3, 'key': 18, 'sum': 88},
                           {'height': 2, 'key': 28, 'sum': 58},
                           {'height': 1, 'key': 30, 'sum': 30}], i_set.in_order(node))
        i_set.add(3)
        node = i_set.add(2)
        self.assertEquals([{'key': 2, 'sum': 2, 'height': 1},
                           {'key': 3, 'sum': 9, 'height': 2},
                           {'key': 4, 'sum': 4, 'height': 1},
                           {'key': 5, 'sum': 20, 'height': 3},
                           {'key': 6, 'sum': 6, 'height': 1},
                           {'key': 8, 'sum': 116, 'height': 4},
                           {'key': 12, 'sum': 12, 'height': 1},
                           {'key': 18, 'sum': 88, 'height': 3},
                           {'key': 28, 'sum': 58, 'height': 2},
                           {'key': 30, 'sum': 30, 'height': 1}], i_set.in_order(node))
        node = i_set.remove(6)
        self.assertEquals([{'height': 1, 'key': 2, 'sum': 2},
                           {'height': 3, 'key': 3, 'sum': 14},
                           {'height': 1, 'key': 4, 'sum': 4},
                           {'height': 2, 'key': 5, 'sum': 9},
                           {'height': 4, 'key': 8, 'sum': 110},
                           {'height': 1, 'key': 12, 'sum': 12},
                           {'height': 3, 'key': 18, 'sum': 88},
                           {'height': 2, 'key': 28, 'sum': 58},
                           {'height': 1, 'key': 30, 'sum': 30}], i_set.in_order(node))
        node = i_set.remove(30)
        self.assertEquals([{'height': 1, 'key': 2, 'sum': 2},
                           {'height': 3, 'key': 3, 'sum': 14},
                           {'height': 1, 'key': 4, 'sum': 4},
                           {'height': 2, 'key': 5, 'sum': 9},
                           {'height': 4, 'key': 8, 'sum': 80},
                           {'height': 1, 'key': 12, 'sum': 12},
                           {'height': 2, 'key': 18, 'sum': 58},
                           {'height': 1, 'key': 28, 'sum': 28}], i_set.in_order(node))
        i_set.remove(12)
        node = i_set.remove(18)
        self.assertEquals([{'key': 2, 'sum': 2, 'height': 1},
                           {'key': 3, 'sum': 9, 'height': 2},
                           {'key': 4, 'sum': 4, 'height': 1},
                           {'key': 5, 'sum': 50, 'height': 3},
                           {'key': 8, 'sum': 36, 'height': 2},
                           {'key': 28, 'sum': 28, 'height': 1}], i_set.in_order(node))
        i_set.remove(8)
        node = i_set.remove(28)
        self.assertEquals([{'key': 2, 'height': 1, 'sum': 2},
                           {'key': 3, 'height': 3, 'sum': 14},
                           {'key': 4, 'height': 1, 'sum': 4},
                           {'key': 5, 'height': 2, 'sum': 9}], i_set.in_order(node))
        i_set.add(5)
        i_set.add(2)
        node = i_set.add(3)
        self.assertEquals([{'key': 2, 'height': 1, 'sum': 2},
                           {'key': 3, 'height': 3, 'sum': 14},
                           {'key': 4, 'height': 1, 'sum': 4},
                           {'key': 5, 'height': 2, 'sum': 9}], i_set.in_order(node))
        i_set.remove(8)
        node = i_set.remove(28)
        self.assertEquals([{'key': 2, 'height': 1, 'sum': 2},
                           {'key': 3, 'height': 3, 'sum': 14},
                           {'key': 4, 'height': 1, 'sum': 4},
                           {'key': 5, 'height': 2, 'sum': 9}], i_set.in_order(node))

    def test_find_in_set(self):
        i_set = IntervalSet()
        i_set.add(5)
        i_set.add(12)
        i_set.add(4)
        i_set.add(6)
        i_set.add(8)
        i_set.add(18)
        node = i_set.add(28)
        self.assertEqual(12, AVLTree.find(12, node).key)
        self.assertEqual(8, AVLTree.find(8, node).key)
        self.assertEqual(5, AVLTree.find(5, node).key)
        self.assertEqual(None, AVLTree.find(125, node))
        self.assertEqual(None, AVLTree.find(1250, node))
        i_set.remove(5)
        node = i_set.remove(18)
        self.assertEqual(None, AVLTree.find(5, node))
        self.assertEqual(None, AVLTree.find(18, node))
