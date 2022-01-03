from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from tkcalendar import Calendar,DateEntry
from back_end.Connection import *
import back_end.Connection
from model.tea_model_class import *
import model.tea_model_class
from tkinter import messagebox
import tkinter.messagebox

# import front_end.view_tea
# from front_end.view_tea import *






class tea_manage:
    def __init__(self,window):
        self.wn=window
        self.wn.title('Tea Management')
        self.wn.geometry('750x700+450+70')
        self.wn.resizable=(False,False)

        #creating connection object
        self.dconnect=databaseConnection()

        #textvariables
        self.customer_id=StringVar()
        self.customer_name = StringVar()
        self.customer_address = StringVar()
        self.grading = StringVar()
        self.tea_leaves = StringVar()
        self.date = StringVar()

        self.lbl_heading = Label(self.wn, text='Tea Leaf Management System', bg='black', fg='#81d95b'
                                 , font=('arial', 14, 'bold'))

        self.lbl_heading.pack(side=TOP, fill=X)

        self.bgimg = ImageTk.PhotoImage(file='C:\\python danphe\\front_end\\images\\teabg.jpg')

        bgLabel = Label(self.wn, image=self.bgimg).pack()

        #frame
        lbl_frame=Frame(self.wn, relief=SOLID,bg='#1c4485')
        lbl_frame.place(x=150,y=100,height=410,width=450)

        btn_frame = Frame(self.wn, relief=SOLID, bg='#3073f0')
        btn_frame.place(x=150, y=525, height=55, width=450)

        #labels
        lbl_customerid = Label(lbl_frame, text='Customer ID  ', font=('Goudy old style', 16, 'bold'), bg='#1c4485',
                             fg='white')
        lbl_customerid.grid(row=0, column=0, pady=20)

        lbl_customer=Label(lbl_frame,text='Customer Name',font=('Goudy old style', 16, 'bold'),bg='#1c4485',fg='white')
        lbl_customer.grid(row=1,column=0,pady=20)

        lbl_address = Label(lbl_frame, text='  Address  ', font=('Goudy old style', 16, 'bold'),bg='#1c4485',fg='white')
        lbl_address.grid(row=2, column=0,pady=20)

        lbl_grading = Label(lbl_frame, text='  Grading  ', font=('Goudy old style', 16, 'bold'),bg='#1c4485',fg='white')
        lbl_grading.grid(row=3, column=0,pady=20)

        lbl_leaves = Label(lbl_frame, text='Tea Leaves(kg)', font=('Goudy old style', 16, 'bold'),bg='#1c4485',fg='white')
        lbl_leaves.grid(row=4, column=0,pady=20)





        lbl_date = Label(lbl_frame, text='  Date  ', font=('Goudy old style', 16, 'bold'),bg='#1c4485',fg='white')
        lbl_date.grid(row=5, column=0,pady=20)

        #entries
        ent_customerid = Entry(lbl_frame,textvariable=self.customer_id, bg='#1c4485', fg='white', font=('Goudy old style', 16, 'bold'), bd=3)
        ent_customerid.grid(row=0, column=1, padx=10)

        ent_customer=Entry(lbl_frame,bg='#1c4485',textvariable=self.customer_name, fg='white',font=('Goudy old style', 16, 'bold'),bd=3)
        ent_customer.grid(row=1,column=1,padx=10)

        ent_address = Entry(lbl_frame, bg='#1c4485', textvariable=self.customer_address, fg='white',font=('Goudy old style', 16, 'bold'),bd=3)
        ent_address.grid(row=2, column=1, padx=10)

        combo_grading = ttk.Combobox(lbl_frame ,font=('arial', 14, 'bold'), textvariable=self.grading, state='readonly')
        combo_grading['values'] = ('A+', 'A-', 'A', 'B', 'C')
        combo_grading.grid(row=3, column=1, padx=12, pady=10, sticky='w')


        ent_leaves = Entry(lbl_frame, bg='#1c4485',textvariable=self.tea_leaves,  fg='white',font=('Goudy old style', 16, 'bold'),bd=3)
        ent_leaves.grid(row=4, column=1, padx=10)

        ent_date= DateEntry(lbl_frame, textvariable=self.date, bg='#1c4485', fg='white',font=('Goudy old style', 16, 'bold'),bd=3,year=2020)
        ent_date.grid(row=5, column=1,padx=1)

        btn_add = Button(btn_frame, text=' Add', font=('arial', 14, 'bold'), bd=2, bg='#4789ed', fg='white',
                         relief=GROOVE,command=self.add_error)
        btn_add.pack(side=LEFT, padx=10)

        btn_delete = Button(btn_frame, text='Delete', font=('arial', 14, 'bold'), bd=2, bg='#4789ed', fg='white',
                         relief=GROOVE,command=self.delete_error)
        btn_delete.pack(side=LEFT, padx=10)

        btn_update= Button(btn_frame, text='Update', font=('arial', 14, 'bold'), bd=2, bg='#4789ed', fg='white',
                         relief=GROOVE,command=self.update_error)
        btn_update.pack(side=LEFT, padx=10)

        btn_clear= Button(btn_frame, text='Clear', font=('arial', 14, 'bold'), bd=2, bg='#4789ed', fg='white',
                         relief=GROOVE,command=self.clear)
        btn_clear.pack(side=LEFT, padx=10)

        # btn_view = Button(btn_frame, text='View', font=('arial', 14, 'bold'), bd=2, bg='#4789ed', fg='white',
        #                    relief=GROOVE, command=self.tea_view)
        # btn_view.pack(side=LEFT, padx=10)

    def add_error(self):
        if self.customer_id.get()=='' or self.customer_name.get()=='' and self.tea_leaves.get()=='' or self.grading.get()=='':
            messagebox.showerror('Error','Please fill all fields')
        else:
            self.add()


    def add(self):
        try:

            tea_obj =Tea_model(self.customer_id.get(), self.customer_name.get(), self.customer_address.get(), self.grading.get(),
                                 self.tea_leaves.get(),
                                 self.date.get())
            query = 'insert into tea_manage values(%s,%s,%s,%s,%s,%s);'
            values = (tea_obj.get_id(),tea_obj.get_name(),tea_obj.get_address(),tea_obj.get_grading(),tea_obj.get_leaves(),tea_obj.get_date())

            self.dconnect.add2(query, values)
            messagebox.showinfo('Success', 'Record inserted successfully')

            self.clear()
        except:
            tkinter.messagebox.showerror('Error','Key is already taken')


    def update_error(self):
        if self.customer_id.get()=='' :
            messagebox.showerror('Error','Please choose id to update')
        else:
            self.update()
    def update(self):
        try:

            tea_obj = Tea_model(self.customer_id.get(), self.customer_name.get(), self.customer_address.get(), self.grading.get(),
                                 self.tea_leaves.get(),
                                 self.date.get())
            query = 'update tea_manage set customer_name=%s,customer_address=%s,grading=%s,tea_leaves=%s,date=%s where customer_id=%s;'
            customer_id=self.customer_id.get()
            customer_name=self.customer_name.get()
            customer_address=self.customer_address.get()
            grading=self.grading.get()
            tea_leaves=self.tea_leaves.get()
            date=self.date.get()
            values = (customer_name,customer_address,grading,tea_leaves,date,customer_id)
            self.dconnect.update2(query, values)
            messagebox.showinfo('Success', 'Record updated successfully')
            self.clear()
        except:
            tkinter.messagebox.showerror('Error', 'Select Valid ID')
    def clear(self):
        self.customer_id.set('')
        self.customer_name.set('')
        self.customer_address.set('')
        self.grading.set('')
        self.tea_leaves.set('')
        self.date.set('')

    def delete_error(self):

        if self.customer_id.get() == '':
            messagebox.showerror('Error', 'Please choose id to delete')
        else:
            self.delete()

    def delete(self):
        try:
            query = 'delete from tea_manage where customer_id=%s;'
            customer_id = self.customer_id.get()
            values = (customer_id,)
            self.dconnect.delete2(query, values)
            messagebox.showinfo("Success", ' Record deleted successfully ')
        except:
            tkinter.messagebox.showerror('Error', 'Select Valid ID')




# wn=Tk()
# objct=tea_manage(wn)
# wn.mainloop()