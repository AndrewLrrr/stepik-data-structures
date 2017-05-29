import unittest

from module2.task3_disjoint_set import DatabaseEmulator


class TestDatabaseEmulator(unittest.TestCase):
    def test_max1(self):
        db = DatabaseEmulator([1, 1, 1, 1, 1])
        joins = [
            (3, 5),
            (2, 4),
            (1, 4),
            (5, 4),
            (5, 3)
        ]
        expected = [2, 2, 3, 5, 5]
        actual = []
        for join in joins:
            db.join(*join)
            actual.append(db.max())
        self.assertEquals(expected, actual)

    def test_max2(self):
        db = DatabaseEmulator([10, 0, 5, 0, 3, 3])
        joins = [
            (6, 6),
            (6, 5),
            (5, 4),
            (4, 3),
        ]
        expected = [10, 10, 10, 11]
        actual = []
        for join in joins:
            db.join(*join)
            actual.append(db.max())
        self.assertEquals(expected, actual)

    def test_max3(self):
        db = DatabaseEmulator([10, 0, 5, 0, 3, 3])
        joins = [
            (6, 6),
            (6, 5),
            (5, 4),
            (4, 3),
            (4, 3),
            (1, 2),
            (1, 6),
        ]
        expected = [10, 10, 10, 11, 11, 11, 21]
        actual = []
        for join in joins:
            db.join(*join)
            actual.append(db.max())
        self.assertEquals(expected, actual)

