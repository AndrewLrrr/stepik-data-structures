import unittest

from module4.task3_check_general_properties_of_binary_tree import Tree
from module4.task3_check_general_properties_of_binary_tree import TreePropertiesChecker


class TestTreePropertiesChecker(unittest.TestCase):
    def test1(self):
        tree = Tree()
        tree_checker = TreePropertiesChecker(tree)
        tree.add(2, 1, 2)
        tree.add(1, -1, -1)
        tree.add(3, -1, -1)
        self.assertEqual('CORRECT', tree_checker.run())

    def test2(self):
        tree = Tree()
        tree_checker = TreePropertiesChecker(tree)
        self.assertEqual('CORRECT', tree_checker.run())

    def test3(self):
        tree = Tree()
        tree_checker = TreePropertiesChecker(tree)
        tree.add(1, -1, -1)
        self.assertEqual('CORRECT', tree_checker.run())

    def test4(self):
        tree = Tree()
        tree_checker = TreePropertiesChecker(tree)
        tree.add(1, 1, 2)
        tree.add(2, -1, -1)
        tree.add(3, -1, -1)
        self.assertEqual('INCORRECT', tree_checker.run())

    def test5(self):
        tree = Tree()
        tree_checker = TreePropertiesChecker(tree)
        tree.add(1, -1, 1)
        tree.add(2, -1, 2)
        tree.add(3, -1, 3)
        tree.add(4, -1, 4)
        tree.add(5, 5, -1)
        tree.add(4, -1, -1)
        self.assertEqual('CORRECT', tree_checker.run())

    def test6(self):
        tree = Tree()
        tree_checker = TreePropertiesChecker(tree)
        tree.add(4, 1, 2)
        tree.add(2, 3, 4)
        tree.add(6, 5, 6)
        tree.add(1, -1, -1)
        tree.add(3, -1, -1)
        tree.add(5, -1, -1)
        tree.add(7, -1, -1)
        self.assertEqual('CORRECT', tree_checker.run())

    def test7(self):
        tree = Tree()
        tree_checker = TreePropertiesChecker(tree)
        tree.add(4, 1, -1)
        tree.add(2, 2, 3)
        tree.add(1, -1, -1)
        tree.add(5, -1, -1)
        self.assertEqual('INCORRECT', tree_checker.run())

    def test8(self):
        tree = Tree()
        tree_checker = TreePropertiesChecker(tree)
        tree.add(10, 1, 8)
        tree.add(5, 2, 3)
        tree.add(3, 4, 5)
        tree.add(8, 6, 7)
        tree.add(2, -1, -1)
        tree.add(4, -1, -1)
        tree.add(6, -1, -1)
        tree.add(9, -1, -1)
        tree.add(12, 9, 10)
        tree.add(11, -1, -1)
        tree.add(16, -1, -1)
        self.assertEqual('CORRECT', tree_checker.run())

    def test9(self):
        tree = Tree()
        tree_checker = TreePropertiesChecker(tree)
        tree.add(10, 1, 8)
        tree.add(5, 2, 3)
        tree.add(3, 4, 5)
        tree.add(8, 6, 7)
        tree.add(2, -1, -1)
        tree.add(4, -1, -1)
        tree.add(6, -1, -1)
        tree.add(9, -1, 11)
        tree.add(12, 9, 10)
        tree.add(11, -1, -1)
        tree.add(16, -1, -1)
        tree.add(12, -1, -1)
        self.assertEqual('INCORRECT', tree_checker.run())

    def test10(self):
        tree = Tree()
        tree_checker = TreePropertiesChecker(tree)
        tree.add(10, 1, 8)
        tree.add(5, 2, 3)
        tree.add(3, 4, 5)
        tree.add(8, 6, 7)
        tree.add(2, -1, -1)
        tree.add(4, -1, -1)
        tree.add(6, -1, -1)
        tree.add(9, -1, -1)
        tree.add(12, 9, 10)
        tree.add(11, 11, -1)
        tree.add(16, -1, -1)
        tree.add(8, -1, -1)
        self.assertEqual('INCORRECT', tree_checker.run())

    def test11(self):
        tree = Tree()
        tree_checker = TreePropertiesChecker(tree)
        tree.add(10, 1, 8)
        tree.add(5, 2, 3)
        tree.add(3, 4, 5)
        tree.add(8, 6, 7)
        tree.add(2, -1, -1)
        tree.add(4, -1, -1)
        tree.add(6, -1, -1)
        tree.add(9, -1, -1)
        tree.add(12, 9, 10)
        tree.add(11, -1, -1)
        tree.add(16, 11, -1)
        tree.add(14, 12, 13)
        tree.add(12, -1, -1)
        tree.add(18, -1, -1)
        self.assertEqual('INCORRECT', tree_checker.run())

    def test12(self):
        tree = Tree()
        tree_checker = TreePropertiesChecker(tree)
        tree.add(10, 1, 8)
        tree.add(5, 2, 3)
        tree.add(3, 4, 5)
        tree.add(8, 6, 7)
        tree.add(2, -1, -1)
        tree.add(4, -1, -1)
        tree.add(6, -1, -1)
        tree.add(9, -1, -1)
        tree.add(12, 9, 10)
        tree.add(11, -1, -1)
        tree.add(16, 11, -1)
        tree.add(14, 12, -1)
        tree.add(12, -1, -1)
        self.assertEqual('CORRECT', tree_checker.run())

    def test13(self):
        tree = Tree()
        tree_checker = TreePropertiesChecker(tree)
        tree.add(-11, 1, 4)
        tree.add(-15, 2, 3)
        tree.add(-16, -1, -1)
        tree.add(-14, -1, -1)
        tree.add(-9, 5, 6)
        tree.add(-10, -1, -1)
        tree.add(1, -1, -1)
        self.assertEqual('CORRECT', tree_checker.run())

    def test14(self):
        tree = Tree()
        tree_checker = TreePropertiesChecker(tree)
        tree.add(2, 1, 2)
        tree.add(2, -1, -1)
        tree.add(3, -1, -1)
        self.assertEqual('INCORRECT', tree_checker.run())

    def test15(self):
        tree = Tree()
        tree_checker = TreePropertiesChecker(tree)
        tree.add(2, 1, 2)
        tree.add(1, -1, -1)
        tree.add(2, -1, -1)
        self.assertEqual('CORRECT', tree_checker.run())
