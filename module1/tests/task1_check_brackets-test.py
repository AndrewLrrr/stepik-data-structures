import unittest

from module1.task1_check_brackets import check_brackets


class TestStack(unittest.TestCase):
    def test_1(self):
        self.assertEqual(-1, check_brackets('()[]'))

    def test_2(self):
        self.assertEqual(5, check_brackets('()[]}'))

    def test_3(self):
        self.assertEqual(7, check_brackets('{{[()]]'))

    def test_4(self):
        self.assertEqual(3, check_brackets('()['))

    def test_5(self):
        self.assertEqual(3, check_brackets('()[{}'))

    def test_6(self):
        self.assertEqual(3, check_brackets('()([{}'))

    def test_7(self):
        self.assertEqual(-1, check_brackets('foo(bar);'))

    def test_8(self):
        self.assertEqual(10, check_brackets('foo(bar[i);'))

    def test_9(self):
        self.assertEqual(4, check_brackets('foo(bar[i;'))
