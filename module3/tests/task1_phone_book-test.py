import unittest

from module3.task1_phone_book import PhoneBook


class TestPhoneBook(unittest.TestCase):
    def test1(self):
        pb = PhoneBook()
        pb.add('911', 'police')
        pb.add('76213', 'Mom')
        pb.add('17239', 'Bob')
        self.assertEqual('Mom', pb.find('76213'))
        self.assertEqual('not found', pb.find('910'))
        self.assertEqual('police', pb.find('911'))
        pb.delete('910')
        pb.delete('911')
        self.assertEqual('not found', pb.find('911'))
        self.assertEqual('Mom', pb.find('76213'))
        pb.add('76213', 'daddy')

    def test2(self):
        pb = PhoneBook()
        self.assertEqual('not found', pb.find('3839442'))
        pb.add('123456', 'me')
        pb.add('0', 'granny')
        self.assertEqual('granny', pb.find('0'))
        self.assertEqual('me', pb.find('123456'))
        pb.delete('0')
        pb.delete('0')
        self.assertEqual('not found', pb.find('0'))
