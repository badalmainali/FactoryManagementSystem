

import unittest
from back_end.Connection import databaseConnection


class test_connection(unittest.TestCase):
    def setUp(self):
        self.values = (1, 'Ram')
        self.values2 = (1,)
        self.dbconnect = databaseConnection()

    def test_add(self):
        query = 'insert into test values(%s,%s);'


        self.dbconnect.add(query, self.values)
        actual = [(1, 'Ram'), ]
        query1 = 'select * from test where id=1;'
        expect = self.dbconnect.select_fetch(query1)
        self.assertEqual(actual, expect)



    def test_delete(self):
        query = 'delete from test where id=%s;'
        values=self.values2

        self.dbconnect.delete(query,values)
        actual = []
        query1 = 'select * from test where id=1;'
        expect = self.dbconnect.select_fetch(query1)
        print('Remaining value:', expect)
        self.assertEqual(actual, expect)

