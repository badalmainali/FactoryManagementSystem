from tkinter import *
from tkinter import ttk
from front_end.tea_main import *
from back_end.Connection import *
from PIL import ImageTk

class view_info:
    def __init__(self,wn):
        self.wn=wn
        self.wn.geometry('600x600+370+80')
        self.wn.title('View Table Tea Status')

        #creating connection
        self.dbconnect=databaseConnection()

        lbl_heading = Label(self.wn, text='Tea Leaves Records View Page', font=('Goudy old style', 22, 'bold'),
                            fg='red', bg='black')
        lbl_heading.pack(side=TOP, fill=X)

        self.bgimg1 = ImageTk.PhotoImage(file='C:\\python danphe\\front_end\\images\\tea_view.jpg')

        self.bgLabel = Label(self.wn, image = self.bgimg1).pack()

        # ........creating Table frame'''''''''''''
        scroll_frame = Frame(self.wn, bd=4, relief=RIDGE, bg='aqua')
        scroll_frame.place(x=5, y=100, width=590, height=400)
        #
        scroll_x = Scrollbar(scroll_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(scroll_frame, orient=VERTICAL)

        self.tea_table = ttk.Treeview(scroll_frame, columns=('customer_id','customer_name','customer_address','grading','tea_leaves','date'),
                                      xscrollcommand=scroll_x,
                                           yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.tea_table.xview)
        scroll_y.config(command=self.tea_table.yview)
        self.tea_table.heading('customer_id', text='ID')
        self.tea_table.heading('customer_name', text=' Name')
        self.tea_table.heading('customer_address', text='Address')
        self.tea_table.heading('grading',text='Grading')
        self.tea_table.heading('tea_leaves',text='Tea Leaves(kg)')
        self.tea_table.heading('date',text='Date')

        self.tea_table.column('customer_id', width=50)
        self.tea_table.column('customer_name', width=80)
        self.tea_table.column('customer_address', width=80)
        self.tea_table.column('grading', width=40)
        self.tea_table.column('tea_leaves', width=80)
        self.tea_table.column('date', width=80)

        self.tea_table['show'] = 'headings'
        self.tea_table.pack(fill=BOTH, expand=1)
        self.fetch_data()

    def fetch_data(self):

        query = 'select * from tea_manage;'
        rows = self.dbconnect.select_two(query)
        if len(rows) != 0:
            self.tea_table.delete(*self.tea_table.get_children())
            for rows in rows:
                self.tea_table.insert('', END, values=rows)
            self.dbconnect.fetch(query)


# wn=Tk()
# obj=view_info(wn)
# wn.mainloop()