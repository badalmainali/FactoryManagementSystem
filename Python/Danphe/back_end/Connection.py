import mysql.connector

class databaseConnection:
    def __init__(self):
        self.con=mysql.connector.connect(host='localhost',user='root',password='badman123',
                                         database='danphe')
        self.my_cursor=self.con.cursor()

    def add(self,query,values):
        self.my_cursor.execute(query,values)
        self.con.commit()

    def update(self,query,values):
        self.my_cursor.execute(query,values)
        self.con.commit()

    def delete(self,query,values):
        self.my_cursor.execute(query,values)
        self.con.commit()

    def select_one(self,query,values):
        self.my_cursor.execute(query,values)
        records=self.my_cursor.fetchall()
        self.con.commit()
        return records

    def select_two(self,query):
        self.my_cursor.execute(query)
        records=self.my_cursor.fetchall()
        self.con.commit()
        return records
    def select_fetch(self,query):
        self.my_cursor.execute(query)
        records=self.my_cursor.fetchall()
        self.con.commit()
        return records


    def fetch(self,query):
        self.my_cursor.execute(query)
        self.rows=self.my_cursor.fetchall()
        self.con.commit()

    def search_data(self, query):
        self.my_cursor.execute(query)
        self.rows = self.my_cursor.fetchall()
        self.con.commit()

    def add2(self,query,values):
        self.my_cursor.execute(query,values)
        self.con.commit()

    def update2(self,query,values):
        self.my_cursor.execute(query,values)
        self.con.commit()

    def delete2(self,query,values):
        self.my_cursor.execute(query,values)
        self.con.commit()





