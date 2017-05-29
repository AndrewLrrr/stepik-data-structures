import unittest

from module2.task4_automatic_analysis_of_programs import VariablesAnalyzer


class TestVariablesAnalyzer(unittest.TestCase):
    def test1(self):
        va = VariablesAnalyzer(5)
        equals = [
            (1, 2),
            (1, 3),
            (1, 4),
            (2, 3),
            (2, 4),
            (3, 4)
        ]
        inequals = [
            (1, 5),
            (2, 5)
        ]
        expected = [True, True, True, False, False, False, True, True]
        actual = []
        for equal in equals:
            actual.append(va.add_equality(*equal))
        for inequal in inequals:
            actual.append(va.add_inequality(*inequal))
        self.assertEquals(expected, actual)

    def test2(self):
        va = VariablesAnalyzer(6)
        equals = [
            (2, 3),
            (1, 5),
            (2, 5),
            (3, 4),
            (4, 2)
        ]
        inequals = [
            (6, 1),
            (4, 6),
            (4, 5)
        ]
        expected = [True, True, True, True, False, True, True, False]
        actual = []
        for equal in equals:
            actual.append(va.add_equality(*equal))
        for inequal in inequals:
            actual.append(va.add_inequality(*inequal))
        self.assertEquals(expected, actual)

    def test3(self):
        va = VariablesAnalyzer(1)
        inequals = [
            (1, 1)
        ]
        expected = [False]
        actual = []
        for inequal in inequals:
            actual.append(va.add_inequality(*inequal))
        self.assertEquals(expected, actual)


