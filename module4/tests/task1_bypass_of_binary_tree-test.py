import unittest

from module4.task1_bypass_of_binary_tree import Tree
from module4.task1_bypass_of_binary_tree import TreeCrawler


class TestTree(unittest.TestCase):
    def test_tree_growing1(self):
        tree = Tree()
        tree.add(4, 1, 2)
        tree.add(2, 3, 4)
        tree.add(5, -1, -1)
        tree.add(1, -1, -1)
        tree.add(3, -1, -1)

        root = tree.get_root()
        self.assertEqual(4, root.value)
        self.assertEqual(2, root.left.value)
        self.assertEqual(5, root.right.value)
        self.assertEqual(1, root.left.left.value)
        self.assertEqual(3, root.left.right.value)

    def test_tree_growing2(self):
        tree = Tree()
        tree.add(0, 7, 2)
        tree.add(10, -1, -1)
        tree.add(20, -1, 6)
        tree.add(30, 8, 9)
        tree.add(40, 3, -1)
        tree.add(50, -1, -1)
        tree.add(60, 1, -1)
        tree.add(70, 5, 4)
        tree.add(80, -1, -1)
        tree.add(90, -1, -1)

        root = tree.get_root()
        self.assertEqual(0, root.value)
        self.assertEqual(70, root.left.value)
        self.assertEqual(20, root.right.value)
        self.assertEqual(50, root.left.left.value)
        self.assertEqual(40, root.left.right.value)
        self.assertEqual(30, root.left.right.left.value)
        self.assertEqual(80, root.left.right.left.left.value)
        self.assertEqual(90, root.left.right.left.right.value)
        self.assertEqual(60, root.right.right.value)
        self.assertEqual(10, root.right.right.left.value)


class TestCrawler(unittest.TestCase):
    def setUp(self):
        self.tree1 = Tree()
        self.tree1.add(4, 1, 2)
        self.tree1.add(2, 3, 4)
        self.tree1.add(5, -1, -1)
        self.tree1.add(1, -1, -1)
        self.tree1.add(3, -1, -1)

        self.tree2 = Tree()
        self.tree2.add(0, 7, 2)
        self.tree2.add(10, -1, -1)
        self.tree2.add(20, -1, 6)
        self.tree2.add(30, 8, 9)
        self.tree2.add(40, 3, -1)
        self.tree2.add(50, -1, -1)
        self.tree2.add(60, 1, -1)
        self.tree2.add(70, 5, 4)
        self.tree2.add(80, -1, -1)
        self.tree2.add(90, -1, -1)

    def test_tree_in_order_bypass(self):
        tree_crawler = TreeCrawler(self.tree1)
        self.assertEquals([1, 2, 3, 4, 5], tree_crawler.in_order())
        tree_crawler2 = TreeCrawler(self.tree2)
        self.assertEquals([50, 70, 80, 30, 90, 40, 0, 20, 10, 60], tree_crawler2.in_order())

    def test_tree_pre_order_bypass(self):
        tree_crawler = TreeCrawler(self.tree1)
        self.assertEquals([4, 2, 1, 3, 5], tree_crawler.pre_order())
        tree_crawler2 = TreeCrawler(self.tree2)
        self.assertEquals([0, 70, 50, 40, 30, 80, 90, 20, 60, 10], tree_crawler2.pre_order())

    def test_tree_post_order_bypass(self):
        tree_crawler = TreeCrawler(self.tree1)
        self.assertEquals([1, 3, 2, 5, 4], tree_crawler.post_order())
        tree_crawler = TreeCrawler(self.tree2)
        self.assertEquals([50, 80, 90, 30, 40, 70, 10, 60, 20, 0], tree_crawler.post_order())

    def test_several_orders_for_one_tree(self):
        tree_crawler = TreeCrawler(self.tree1)
        self.assertEquals([1, 2, 3, 4, 5], tree_crawler.in_order())
        self.assertEquals([4, 2, 1, 3, 5], tree_crawler.pre_order())
        self.assertEquals([1, 3, 2, 5, 4], tree_crawler.post_order())
