import unittest
from front_end.emp import *
from model.empl import *

class test_employee(unittest.TestCase):
    def setUp(self):
        self.val=Employees(1,'Hari','Karki','Master','hari@gmail','ktm','22','Male','983434434','IT','Intern','34535345')
        self.val1 = Employees(1, 'Ram', 'Oli', 'Bachelor', 'ram@gmail', 'pokhara', '23', 'Male', '983434233', 'Security',
                             'Senior', '34535345')

    def test_get_fname(self):
        self.assertEqual('Hari',self.val.get_fname())
        self.assertEqual('Ram',self.val1.get_fname())

    def test_get_lname(self):
        self.assertEqual('Karki',self.val.get_lname())
        self.assertEqual('Oli',self.val1.get_lname())

    def test_get_qual(self):
        self.assertEqual('Master',self.val.get_qual())
        self.assertEqual('Bachelor',self.val1.get_qual())

    def test_get_email(self):
        self.assertEqual('hari@gmail',self.val.get_email())
        self.assertEqual('ram@gmail',self.val1.get_email())

    def test_get_address(self):
        self.assertEqual('ktm',self.val.get_address())
        self.assertEqual('pokhara',self.val1.get_address())
    def test_get_age(self):
        self.assertEqual('22',self.val.get_age())
        self.assertEqual('23',self.val1.get_age())

    def test_get_gender(self):
        self.assertEqual('Male',self.val.get_gender())
        self.assertEqual('Male',self.val1.get_gender())

    def test_get_contact(self):
        self.assertEqual('983434434',self.val.get_contact())
        self.assertEqual('983434233',self.val1.get_contact())

    def test_get_faculty(self):
        self.assertEqual('IT',self.val.get_faculty())
        self.assertEqual('Security',self.val1.get_faculty())

    def test_get_post(self):
        self.assertEqual('Intern',self.val.get_post())
        self.assertEqual('Senior',self.val1.get_post())

    def test_get_citizen(self):
        self.assertEqual('34535345',self.val.get_citizen())
        self.assertEqual('34535345',self.val1.get_citizen())



