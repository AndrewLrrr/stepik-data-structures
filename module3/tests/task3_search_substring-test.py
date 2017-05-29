import unittest

from module3.task3_search_substring import search_substring


class TestSearchSubstring(unittest.TestCase):
    def test1(self):
        self.assertEquals([0, 4], search_substring('abacaba', 'aba'))

    def test2(self):
        self.assertEquals([4], search_substring('testTesttesT', 'Test'))

    def test3(self):
        self.assertEquals([1, 2, 3], search_substring('baaaaaaa', 'aaaaa'))

    def test4(self):
        self.assertEquals([0], search_substring('a', 'a'))

    def test5(self):
        self.assertEquals([0, 1], search_substring('aaa', 'aa'))

    def test6(self):
        self.assertEquals([], search_substring('aAa', 'aa'))
