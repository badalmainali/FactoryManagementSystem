from tkinter import *
from tkinter import ttk
from back_end.Connection import *
from tkinter import messagebox
from model.empl import *


class Employee:
    def __init__(self,wn):
        self.wn=wn
        self.wn.geometry('1460x860+60+20')
        self.wn.title('Employees Management')

        #creating the connection object
        self.dbconnect=databaseConnection()

        #creating the title
        title=Label(self.wn,text='Danphe Employee Management System',font=('Goudy old style',24,'bold'),
                    bg='black',fg='white',bd=3,relief=FLAT)
        title.pack(side=TOP,fill=X)
        #=========all variables==========
        self.id_var=StringVar()
        self.fname_var = StringVar()
        self.lname_var = StringVar()
        self.qual_var = StringVar()
        self.email_var = StringVar()
        self.address_var =StringVar()
        self.age_var =StringVar()
        self.gender_var =StringVar()
        self.contact_var =StringVar()
        self.faculty_var = StringVar()
        self.post_var=StringVar()
        self.citizen_var = StringVar()

        self.search_by=StringVar()
        self.text_search=StringVar()
        self.sort_val=StringVar()

        # creating manage frame
        frame = Frame(self.wn, bd=3, relief=SOLID, bg='#3d55db')
        frame.place(x=25, y=70, width=390, height=630)

        btn_frame=Frame(self.wn,relief=SOLID,bg='#d33ddb',bd=5)
        btn_frame.place(x=25,y=710,height=60,width=390)

        title1 = Label(frame, text="Manage Employees", font=('Times', 16, 'bold', 'bold'), bd=2,
                       fg='black',relief=FLAT)
        title1.grid(row=0, columnspan=2, padx=105)

        lbl_id = Label(frame, text='     ID       ', font=('arial', 15, 'bold'), bg='black', fg='white')
        lbl_id.grid(row=2, column=0, padx=5, pady=8, sticky='w')

        lbl_fname = Label(frame, text='   FName ', font=('arial', 15, 'bold'), bg='black', fg='white')
        lbl_fname.grid(row=3, column=0, padx=5, pady=8, sticky='w')
        lbl_lname = Label(frame, text='   LName ', font=('arial', 15, 'bold'), bg='black', fg='white')
        lbl_lname.grid(row=4, column=0, padx=5, pady=8, sticky='w')

        lbl_qual = Label(frame, text=' Qualif.    ', font=('arial', 15, 'bold'), bg='black', fg='white')
        lbl_qual.grid(row=5, column=0, padx=5, pady=8, sticky='w')

        lbl_email = Label(frame, text='   Email    ', font=('arial', 15, 'bold'), bg='black', fg='white')
        lbl_email.grid(row=6, column=0, padx=5, pady=8, sticky='w')

        lbl_address = Label(frame, text=' Address ', font=('arial', 15, 'bold'), bg='black', fg='white')
        lbl_address.grid(row=7, column=0, padx=5 ,pady=8, sticky='w')

        lbl_age = Label(frame, text='     Age    ', font=('arial', 15, 'bold'), bg='black', fg='white')
        lbl_age.grid(row=8, column=0, padx=5, pady=8, sticky='w')
        lbl_gender = Label(frame, text='  Gender ', font=('arial', 15, 'bold'), bg='black', fg='white')
        lbl_gender.grid(row=9, column=0, padx=5, pady=8, sticky='w')

        lbl_contact = Label(frame, text=' Contact ', font=('arial', 15, 'bold'), bg='black', fg='white')
        lbl_contact.grid(row=10, column=0, padx=5, pady=8, sticky='w')

        lbl_deprt = Label(frame, text='  Faculty ', font=('arial', 15, 'bold'), bg='black', fg='white')
        lbl_deprt.grid(row=11, column=0, padx=5, pady=8, sticky='w')

        lbl_post = Label(frame, text='   Post    ', font=('arial', 15, 'bold'), bg='black', fg='white')
        lbl_post.grid(row=12, column=0, padx=5, pady=8, sticky='w')
        lbl_citizen = Label(frame, text='CitizenNo', font=('arial', 15, 'bold'), bg='black', fg='white')
        lbl_citizen.grid(row=13, column=0, padx=5, pady=8, sticky='w')

        ent_id = Entry(frame, textvariable=self.id_var, font=('arial', 14, 'bold'), bd=3, relief=GROOVE)
        ent_id.grid(row=2, column=1, padx=15, pady=10, sticky='w')

        ent_fname = Entry(frame, textvariable=self.fname_var, font=('arial', 14, 'bold'), bd=3, relief=GROOVE)
        ent_fname.grid(row=3, column=1, padx=15, pady=10, sticky='w')
        ent_lname = Entry(frame, textvariable=self.lname_var, font=('arial', 14, 'bold'), bd=3, relief=GROOVE)
        ent_lname.grid(row=4, column=1, padx=15, pady=10, sticky='w')

        combo_qual = ttk.Combobox(frame, textvariable=self.qual_var, font=('arial', 14, 'bold'), state='readonly')
        combo_qual['values'] = ('+2', 'Bachelor', 'Master','Other')
        combo_qual.grid(row=5, column=1, padx=12, pady=10, sticky='w')

        ent_email = Entry(frame, textvariable=self.email_var, font=('arial', 14, 'bold'), bd=3, relief=GROOVE)
        ent_email.grid(row=6, column=1, padx=15, pady=10, sticky='w')

        ent_address = Entry(frame, textvariable=self.address_var, font=('arial', 14, 'bold'), bd=3, relief=GROOVE)
        ent_address.grid(row=7, column=1, padx=15, pady=10, sticky='w')

        ent_age = Entry(frame, textvariable=self.age_var, font=('arial', 14, 'bold'), bd=3, relief=GROOVE)
        ent_age.grid(row=8, column=1, padx=15, pady=10, sticky='w')

        combo_gender = ttk.Combobox(frame, textvariable=self.gender_var, font=('arial', 14, 'bold'), state='readonly')
        combo_gender['values'] = ('Male', 'Female', 'Others')
        combo_gender.grid(row=9, column=1, padx=12, pady=10, sticky='w')

        ent_contact = Entry(frame, textvariable=self.contact_var, font=('arial', 14, 'bold'), bd=3, relief=GROOVE)
        ent_contact.grid(row=10, column=1, padx=15, pady=10, sticky='w')

        combo_dept = ttk.Combobox(frame, textvariable=self.faculty_var, font=('arial', 14, 'bold'), state='readonly')
        combo_dept['values'] = ('Security', 'IT', 'Supervising','Accountancy')
        combo_dept.grid(row=11, column=1, padx=12, pady=10, sticky='w')

        combo_post = ttk.Combobox(frame, textvariable=self.post_var, font=('arial', 14, 'bold'), state='readonly')
        combo_post['values'] = ('Intern', 'Senior', 'Manager', 'Expert')
        combo_post.grid(row=12, column=1, padx=12, pady=10, sticky='w')

        ent_citizen = Entry(frame, textvariable=self.citizen_var, font=('arial', 14, 'bold'), bd=3, relief=GROOVE)
        ent_citizen.grid(row=13, column=1, padx=15, pady=10, sticky='w')

        # adding buttons inside the button frame
        btn_add = Button(btn_frame, text='Add', font=('arial', 12, 'bold'), bd=2, bg='#4789ed', fg='white',
                         relief=SOLID,command=self.add_error)
        btn_add.pack(side=LEFT, padx=15)

        btn_update = Button(btn_frame, text='Update', font=('arial', 12, 'bold'), bd=2, bg='#4789ed', fg='white',
                            relief=SOLID, padx=5,command=self.update_error)
        btn_update.pack(side=LEFT, padx=5)

        btn_delete = Button(btn_frame, text='Delete', font=('arial', 12, 'bold'), bd=2, bg='#4789ed', fg='white',
                            relief=SOLID, padx=8,command=self.delete_error)
        btn_delete.pack(side=LEFT, padx=7)

        btn_clear = Button(btn_frame, text='Clear', font=('arial', 12, 'bold'), bd=2, bg='#4789ed', fg='white',
                           relief=SOLID, padx=5,command=self.clear)
        btn_clear.pack(side=LEFT, padx=4)


        # creating  view table frame
        view_frame = Frame(self.wn, bd=3, relief=RIDGE, bg='#b1eb34')
        view_frame.place(x=445, y=70, width=980, height=690)

        lbl_search = Label(view_frame, text='Search By', bg='crimson', fg='white',
                           font=('arial', 12, 'bold'))
        lbl_search.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        combo_search = ttk.Combobox(view_frame,textvariable=self.search_by, font=('arial', 12, 'bold'), width=10, state='readonly')
        combo_search['values'] = ('ID')
        combo_search.grid(row=0, column=1, padx=5, pady=5, sticky='w')


        txt_search = Entry(view_frame, textvariable=self.text_search,font=('arial', 12, 'bold'), bd=3, relief=GROOVE)
        txt_search.grid(row=0, column=2, padx=15, pady=10, sticky='w')

        search_btn = Button(view_frame, text='Search', width=10,command=self.search).grid(row=0, column=3, padx=10, pady=10)
        show_btn = Button(view_frame, text='Show All', width=10,command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)
        btn_sort = Button(view_frame, text='Sort▲',relief=RIDGE, padx=5,command=self.sort_asc).grid(row=0, column=6, padx=10, pady=10)
        btn_sort2 = Button(view_frame, text='Sort▼ ', relief=RIDGE, padx=5, command=self.sort_desc).grid(row=0, column=7,
                                                                                                       padx=10, pady=10)



        #........creating Table frame'''''''''''''
        scroll_frame=Frame(view_frame,bd=4,relief=RIDGE,bg='red')
        scroll_frame.place(x=60,y=70,width=830,height=540)
        #
        scroll_x = Scrollbar(scroll_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(scroll_frame, orient=VERTICAL)

        self.employee_table = ttk.Treeview(scroll_frame, columns=('id','fname','lname','qual','email',
                                                                'address', 'age', 'gender','contact','faculty','post','citizen'),
                                           xscrollcommand=scroll_x,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        self.employee_table.heading('id', text='ID')
        self.employee_table.heading('lname', text='LName')
        self.employee_table.heading('fname', text='FName')

        self.employee_table.heading('qual', text='Qualf')
        self.employee_table.heading('email', text='Email')
        self.employee_table.heading('address', text='Address')
        self.employee_table.heading('age', text='Age')
        self.employee_table.heading('gender', text='Gender')
        self.employee_table.heading('contact', text='Contact')
        self.employee_table.heading('faculty', text='Faculty')
        self.employee_table.heading('post', text='Post')
        self.employee_table.heading('citizen', text='Citizen')
        self.employee_table.column('id', width=50)
        self.employee_table.column('lname', width=60)
        self.employee_table.column('fname', width=60)

        self.employee_table.column('qual', width=60)
        self.employee_table.column('email', width=60)
        self.employee_table.column('address', width=60)
        self.employee_table.column('age', width=35)
        self.employee_table.column('gender', width=60)
        self.employee_table.column('contact', width=60)
        self.employee_table.column('faculty', width=60)
        self.employee_table.column('post', width=50)
        self.employee_table.column('citizen', width=60)
        self.employee_table['show'] = 'headings'
        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind('<ButtonRelease-1>',self.get_cursor)

        #calling fetch data to fill
        self.fetch_data()

    def clear(self):
        self.id_var.set('')
        self.fname_var.set('')
        self.lname_var.set('')
        self.qual_var.set('')
        self.email_var.set('')
        self.address_var.set('')
        self.age_var.set('')
        self.gender_var.set('')
        self.contact_var.set('')
        self.faculty_var.set('')
        self.post_var.set('')
        self.citizen_var.set('')
    def add_error(self):
        if self.id_var.get()=='' or self.fname_var.get()=='' and self.qual_var.get()=='' or self.citizen_var.get()=='':
            messagebox.showerror('Error','Please fill all fields')
        else:
            self.add()


    def add(self):
        try:
            empl_obj=Employees(self.id_var.get(),self.fname_var.get(),self.lname_var.get(),self.qual_var.get(),self.email_var.get(),
                               self.address_var.get(),self.age_var.get(),self.gender_var.get(),self.contact_var.get(),self.faculty_var.get(),
                               self.post_var.get(),self.citizen_var.get())
            query='insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            values=(empl_obj.get_id(),empl_obj.get_fname(),empl_obj.get_lname(),empl_obj.get_qual(),empl_obj.get_email(),
                    empl_obj.get_address(),empl_obj.get_age(),empl_obj.get_gender(),empl_obj.get_contact(),empl_obj.get_faculty(),
                    empl_obj.get_post(),empl_obj.get_citizen())

            self.dbconnect.add(query,values)
            messagebox.showinfo('Success','Record inserted successfully')
            self.clear()

            self.fetch_data()
        except:
            messagebox.showerror('Error', 'Key is already taken')

    def update_error(self):
        if self.id_var.get()=='':
            messagebox.showerror('Error','Select ID please.')
        else:
            self.update()

    def update(self):


        empl_obj=Employees(self.id_var.get(),self.fname_var.get(),self.lname_var.get(),self.qual_var.get(),
                           self.email_var.get(),self.address_var.get(),
                           self.age_var.get(),self.gender_var.get(),self.contact_var.get(),self.faculty_var.get(),
                           self.post_var.get(),self.citizen_var.get())
        query='update employee set fname=%s,lname=%s,qual=%s,email=%s,address=%s,age=%s,' \
              'gender=%s,contact=%s,faculty=%s,post=%s,citizen=%s where id=%s;'
        id=self.id_var.get()
        fname=self.fname_var.get()
        lname=self.lname_var.get()
        qual=self.qual_var.get()
        email=self.email_var.get()
        address=self.address_var.get()
        age=self.age_var.get()
        gender=self.gender_var.get()
        contact=self.contact_var.get()
        faculty=self.faculty_var.get()
        post=self.post_var.get()
        citizen=self.citizen_var.get()
        values=(fname,lname,qual,email,address,age,gender,contact,faculty,post,citizen,id)
        self.dbconnect.update(query,values)

        messagebox.showinfo( "Success",' Record updated successfully ')
        self.fetch_data()

    def delete_error(self):
        if self.id_var.get()=='':
            messagebox.showerror('Error','Please Select ID')
        else:
            self.delete()

    def delete(self):
        query='delete from employee where id=%s;'
        id=self.id_var.get()
        values=(id,)
        self.dbconnect.delete(query,values)
        messagebox.showinfo("Success", ' Record deleted successfully ')
        self.fetch_data()



    def fetch_data(self):

        query='select * from employee'
        rows=self.dbconnect.select_fetch(query)
        if len(rows)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for rows in rows:
                self.employee_table.insert('',END,values=rows)
            self.dbconnect.fetch(query)
    def get_cursor(self,ab):
        cursor_val=self.employee_table.focus()
        contents=self.employee_table.item(cursor_val)
        rows=contents['values']
        self.id_var.set(rows[0])
        self.fname_var.set(rows[1])
        self.lname_var.set(rows[2])
        self.qual_var.set(rows[3])
        self.email_var.set(rows[4])
        self.address_var.set(rows[5])
        self.age_var.set(rows[6])
        self.gender_var.set(rows[7])
        self.contact_var.set(rows[8])
        self.faculty_var.set(rows[9])
        self.post_var.set(rows[10])
        self.citizen_var.set(rows[11])
    def search(self):
        query = "select id from employee;"
        records = self.dbconnect.select_one(query, str(self.text_search.get()),)
        data_list = []
        for row in records:
            data_list.append(row[0])
        ans = self.linear_search(data_list, int(self.text_search.get()))
        print(f"this is linear data{ans}")
        if ans:
            # messagebox.showinfo('Success', 'Move to data')
            query = "select * from employee where id=%s;"
            values = (ans,)
            records1 = self.dbconnect.select_one(query, values)
            if len(records1) != 0:
                self.employee_table.delete(*self.employee_table.get_children())
                for row in records1:
                    self.employee_table.insert('', END, values=row)
        else:
            messagebox.showerror('error', 'not found')
            return

    @classmethod
    def linear_search(cls, data, item):
        for i in range(len(data)):
            if data[i] == item:
                return data[i]
        return False


    # =================== asc sorting ==========================
    def sort_asc(self):
        query = "select * from employee;"
        records = self.dbconnect.select_fetch(query)
        data_list = []
        for row in records:
            data_list.append(row)
        self.sort_ascending(data_list)
        if len(data_list) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data_list:
                self.employee_table.insert('', END, values=i)
        messagebox.showinfo('Successfully Sorted', ' List has been sorted in Ascending Order')

    @classmethod
    def sort_ascending(cls, list1):
        for j in range(len(list1) - 1):
            for i in range(len(list1) - 1):
                if str(list1[i]) > str(list1[i + 1]):
                    list1[i], list1[i + 1] = list1[i + 1], list1[i]
        return list1

    # =================== desc sorting ==========================
    def sort_desc(self):
        query = "select * from employee;"
        records = self.dbconnect.select_fetch(query)
        data_list = []
        for row in records:
            data_list.append(row)
        self.sort_descending(data_list)
        if len(data_list) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data_list:
                self.employee_table.insert('', END, values=i)
        messagebox.showinfo('Successfully Sorted', ' List has been sorted in Descending Order')

    @classmethod
    def sort_descending(cls, list1):
        for j in range(len(list1) + 1):
            for i in range(len(list1) - 1):
                if str(list1[i]) < str(list1[i + 1]):
                    list1[i], list1[i + 1] = list1[i + 1], list1[i]
        return list1



# wn=Tk()
# objec=Employee(wn)
# wn.mainloop()