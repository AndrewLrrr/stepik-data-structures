import unittest

from module1.task4_stack_with_max import StackWithMax


class StackWithMaxTest(unittest.TestCase):
    def test1(self):
        stack = StackWithMax()
        stack.push(2)
        stack.push(1)
        self.assertEqual(2, stack.max())
        self.assertEqual(1, stack.pop())
        self.assertEqual(2, stack.max())

    def test2(self):
        stack = StackWithMax()
        stack.push(1)
        stack.push(2)
        self.assertEqual(2, stack.max())
        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.max())

    def test3(self):
        stack = StackWithMax()
        stack.push(2)
        stack.push(3)
        self.assertEqual(3, stack.max())
        stack.push(9)
        stack.push(7)
        self.assertEqual(9, stack.max())
        stack.push(2)
        self.assertEqual(9, stack.max())
        stack.pop()
        self.assertEqual(9, stack.max())

    def test_throws_exception_if_trying_to_get_max_from_empty_stack(self):
        stack = StackWithMax()
        with self.assertRaises(Exception) as error:
            stack.max()
        self.assertEqual('Stack is empty', str(error.exception))

    def test_throws_exception_if_trying_to_pop_from_empty_stack(self):
        stack = StackWithMax()
        with self.assertRaises(Exception) as error:
            stack.pop()
        self.assertEqual('Stack is empty', str(error.exception))
