import unittest
from front_end.tea_main import *
from model.tea_model_class import *

class test_tea(unittest.TestCase):
    def setUp(self):
        self.value=Tea_model(1,'Harry','US','A','345','12-12-2020')
        self.value1 =Tea_model(2,'David','London','A+','445','10-11-2020')

    def test_get_name(self):
        self.assertEqual('Harry',self.value.get_name())
        self.assertEqual('David',self.value1.get_name())

    def test_get_address(self):
        self.assertEqual('US', self.value.get_address())
        self.assertEqual('London', self.value1.get_address())

    def test_get_grading(self):
        self.assertEqual('A', self.value.get_grading())
        self.assertEqual('A+', self.value1.get_grading())

    def test_get_tea_kg(self):
        self.assertEqual('345', self.value.get_leaves())
        self.assertEqual('445', self.value1.get_leaves())

    def test_get_date(self):
        self.assertEqual('12-12-2020', self.value.get_date())
        self.assertEqual('10-11-2020', self.value1.get_date())

