
import unittest
from front_end.emp import *

class test_record(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5]
        self.data3 = [5, 4, 3, 2, 1]
        self.item1 = 1
        self.item2 = 8
        self.data2 = ['Ram', 'Shyam', 'Hari']
        self.item3 = 'Ram'
        self.item4 = 'Paul'
        self.values = (1, 'Ram', 'Male', '011')
        self.db_connect = databaseConnection()
    def test_linear_search(self):
        self.assertTrue(Employee.linear_search(self.data, self.item1))
        self.assertFalse(Employee.linear_search(self.data, self.item2))
        self.assertTrue(Employee.linear_search(self.data2, self.item3))
        self.assertFalse(Employee.linear_search(self.data2, self.item4))
    def test_sort_ascending(self):
        expect = self.data
        actual = Employee.sort_ascending(self.data3)
        self.assertEqual(actual, expect)
        print(actual, expect)
    def test_sort_descending(self):
        self.assertEqual(self.data3,Employee.sort_descending(self.data))
