import unittest

from module1.task5_slide_max import SlideMaxList


class SlideMaxTest(unittest.TestCase):
    def test1(self):
        size = 1
        values = [2, 1, 5]
        slide_max = SlideMaxList(size, values)
        self.assertEquals([2, 1, 5], list(slide_max))

    def test2(self):
        size = 4
        values = [2, 7, 3, 1, 5, 2, 6, 2]
        slide_max = SlideMaxList(size, values)
        self.assertEquals([7, 7, 5, 6, 6], list(slide_max))

    def test3(self):
        size = 3
        values = [2, 3, 9]
        slide_max = SlideMaxList(size, values)
        self.assertEquals([9], list(slide_max))

    def test4(self):
        size = 3
        values = [2, 7, 3, 8, 5, 6, 4, 3, 1, 9, 11, 5]
        slide_max = SlideMaxList(size, values)
        self.assertEquals([7, 8, 8, 8, 6, 6, 4, 9, 11, 11], list(slide_max))

    def test5(self):
        size = 2
        values = [8, 8, 8, 8, 8, 8]
        slide_max = SlideMaxList(size, values)
        self.assertEquals([8, 8, 8, 8, 8], list(slide_max))

    def test6(self):
        size = 1
        values = [1]
        slide_max = SlideMaxList(size, values)
        self.assertEquals([1], list(slide_max))

    def test7(self):
        size = 2
        values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        slide_max = SlideMaxList(size, values)
        self.assertEquals([10, 9, 8, 7, 6, 5, 4, 3, 2], list(slide_max))

    def test8(self):
        size = 4
        values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        slide_max = SlideMaxList(size, values)
        self.assertEquals([10, 9, 8, 7, 6, 5, 4], list(slide_max))