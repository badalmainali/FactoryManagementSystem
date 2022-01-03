class Tea_model:
    def __init__(self,customer_id,customer_name,customer_address,grading,tea_leaves,date):
        self.customer_id=customer_id
        self.customer_name=customer_name
        self.customer_address=customer_address
        self.grading=grading
        self.tea_leaves=tea_leaves
        self.date=date

    def set_id(self,customer_id):
        self.customer_id = customer_id

    def get_id(self):
        return self.customer_id

    def set_name(self,customer_name):
        self.customer_name=customer_name

    def get_name(self):
        return self.customer_name

    def set_address(self,customer_address):
        self.customer_address=customer_address

    def get_address(self):
        return self.customer_address

    def set_grading(self,grading):
        self.grading=grading

    def get_grading(self):
        return self.grading

    def set_leaves(self,tea_leaves):
        self.tea_leaves=tea_leaves

    def get_leaves(self):
        return self.tea_leaves

    def set_date(self,date):
        self.date=date

    def get_date(self):
        return self.date

