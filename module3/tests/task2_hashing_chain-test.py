import unittest

from module3.task2_hashing_chain import HashTable


class TestHashTable(unittest.TestCase):
    def test1(self):
        ht = HashTable(5)
        ht.add('world')
        ht.add('HellO')
        self.assertEqual('HellO world', ht.check(4))
        self.assertEqual('no', ht.find('World'))
        self.assertEqual('yes', ht.find('world'))
        ht.delete('world')
        self.assertEqual('HellO', ht.check(4))
        ht.delete('HellO')
        ht.add('luck')
        ht.add('GooD')
        self.assertEqual('GooD luck', ht.check(2))
        ht.delete('good')
        self.assertEqual('', ht.check(4))

    def test2(self):
        ht = HashTable(4)
        ht.add('test')
        ht.add('test')
        self.assertEqual('yes', ht.find('test'))
        ht.delete('test')
        self.assertEqual('no', ht.find('test'))
        self.assertEqual('no', ht.find('Test'))
        ht.add('Test')
        self.assertEqual('yes', ht.find('Test'))

    def test3(self):
        ht = HashTable(3)
        self.assertEqual('', ht.check(0))
        self.assertEqual('no', ht.find('help'))
        ht.add('help')
        ht.add('del')
        ht.add('add')
        self.assertEqual('yes', ht.find('add'))
        self.assertEqual('yes', ht.find('del'))
        ht.delete('del')
        self.assertEqual('no', ht.find('del'))
        self.assertEqual('', ht.check(0))
        self.assertEqual('add help', ht.check(1))
        self.assertEqual('', ht.check(2))

    def test4(self):
        ht = HashTable(1)
        ht.add('aaaaaaaaaaaaaaa')
        self.assertEqual('no', ht.find('baaaaaaaaaaaaaa'))
        ht.add('baaaaaaaaaaaaaa')
        self.assertEqual('yes', ht.find('baaaaaaaaaaaaaa'))
        self.assertEqual('baaaaaaaaaaaaaa aaaaaaaaaaaaaaa', ht.check(0))
        ht.delete('baaaaaaaaaaaaaa')
        self.assertEqual('no', ht.find('baaaaaaaaaaaaaa'))
        self.assertEqual('yes', ht.find('aaaaaaaaaaaaaaa'))
        self.assertEqual('aaaaaaaaaaaaaaa', ht.check(0))

    def test5(self):
        ht = HashTable(1)
        ht.add('aa')
        self.assertEqual('no', ht.find('ba'))
        ht.add('ba')
        self.assertEqual('yes', ht.find('ba'))
        self.assertEqual('ba aa', ht.check(0))
        ht.add('aa')
        ht.add('aa')
        self.assertEqual('ba aa', ht.check(0))
        ht.delete('aa')
        self.assertEqual('no', ht.find('aa'))
        self.assertEqual('ba', ht.check(0))
        ht.add('aa')
        self.assertEqual('aa ba', ht.check(0))
        ht.delete('aa')
        ht.delete('ba')
        self.assertEqual('', ht.check(0))

