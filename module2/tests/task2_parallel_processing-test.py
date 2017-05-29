import unittest

from module2.task2_parallel_processing import TaskManager


class TestMinHeap(unittest.TestCase):
    def test1(self):
        processors = 2
        task_times = [1, 2, 3, 4, 5]
        tm = TaskManager(processors)
        expected = [
            (0, 0),
            (1, 0),
            (0, 1),
            (1, 2),
            (0, 4)
        ]
        actual = []
        for task_time in task_times:
            actual.append(tm.add(task_time))

        self.assertEquals(expected, actual)

    def test2(self):
        processors = 2
        task_times = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
        tm = TaskManager(processors)
        expected = [
            (0, 0),
            (1, 0),
            (0, 1),
            (0, 2),
            (1, 2),
            (1, 3),
            (0, 4),
            (0, 5),
            (1, 5),
            (1, 6)
        ]
        actual = []
        for task_time in task_times:
            actual.append(tm.add(task_time))

        self.assertEquals(expected, actual)

    def test3(self):
        processors = 4
        task_times = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        tm = TaskManager(processors)
        expected = [
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (0, 1),
            (1, 1),
            (2, 1),
            (3, 1),
            (0, 2),
            (1, 2),
            (2, 2),
            (3, 2),
            (0, 3),
            (1, 3),
            (2, 3),
            (3, 3),
            (0, 4),
            (1, 4),
            (2, 4),
            (3, 4)
        ]
        actual = []
        for task_time in task_times:
            actual.append(tm.add(task_time))

        self.assertEquals(expected, actual)

    def test4(self):
        processors = 10
        task_times = [0, 0, 0, 1, 0, 0]
        tm = TaskManager(processors)
        expected = [
            (0, 0),
            (0, 0),
            (0, 0),
            (0, 0),
            (1, 0),
            (1, 0)
        ]
        actual = []
        for task_time in task_times:
            actual.append(tm.add(task_time))

        self.assertEquals(expected, actual)

    def test5(self):
        processors = 2
        task_times = [0, 0, 1, 0, 0, 0, 2, 1, 2, 3, 0, 0, 0, 2, 1]
        tm = TaskManager(processors)
        expected = [
            (0, 0),
            (0, 0),
            (0, 0),
            (1, 0),
            (1, 0),
            (1, 0),
            (1, 0),
            (0, 1),
            (0, 2),
            (1, 2),
            (0, 4),
            (0, 4),
            (0, 4),
            (0, 4),
            (1, 5),
        ]
        actual = []
        for task_time in task_times:
            actual.append(tm.add(task_time))

        self.assertEquals(expected, actual)

    def test6(self):
        processors = 4
        task_times = [3, 0, 9, 2, 8, 1, 9, 8, 8, 4]
        tm = TaskManager(processors)
        expected = [
            (0, 0),
            (1, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (2, 2),
            (0, 3),
            (2, 3),
            (3, 8),
            (1, 9)
        ]
        actual = []
        for task_time in task_times:
            actual.append(tm.add(task_time))

        self.assertEquals(expected, actual)

    def test7(self):
        processors = 16
        task_times = [4, 5, 2, 0, 1, 0, 7, 2, 6, 8, 0, 0]
        tm = TaskManager(processors)
        expected = [
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (3, 0),
            (4, 0),
            (4, 0),
            (5, 0),
            (6, 0),
            (7, 0),
            (8, 0),
            (8, 0)
        ]
        actual = []
        for task_time in task_times:
            actual.append(tm.add(task_time))

        self.assertEquals(expected, actual)

    def test8(self):
        processors = 1
        task_times = [2, 0, 4, 3, 9, 8, 4, 9, 0, 4, 3, 2]
        tm = TaskManager(processors)
        expected = [
            (0, 0),
            (0, 2),
            (0, 2),
            (0, 6),
            (0, 9),
            (0, 18),
            (0, 26),
            (0, 30),
            (0, 39),
            (0, 39),
            (0, 43),
            (0, 46)
        ]
        actual = []
        for task_time in task_times:
            actual.append(tm.add(task_time))

        self.assertEquals(expected, actual)
