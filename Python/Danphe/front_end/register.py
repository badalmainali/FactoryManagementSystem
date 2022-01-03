from tkinter import*
import os
import tkinter.messagebox
from PIL import ImageTk
import pickle

d={}

class register_form:
    def __init__(self,window):
        self.wn=window
        self.wn.title('Register')
        self.wn.geometry('550x440+500+150')

        self.lbl_heading = Label(self.wn, text='New Admin Registration Form', bg='black', fg='white'
                              , font=('arial', 14, 'bold'))

        self.lbl_heading.pack(side=TOP, fill=X)

        #creating background image
        self.bgimg = ImageTk.PhotoImage(file='C:\\python danphe\\front_end\\images\\regbg.jpg')

        bgLabel = Label(self.wn, image=self.bgimg).pack()

        # creating frame
        self.frame_one = Frame(self.wn)
        self.frame_one.place(x=120, y=60, height=300, width=300)

        #label and entry
        self.lbl_Fname=Label(self.frame_one,text=' Fname ',font=('arial',12,
                                            'bold'),bg='black',fg='aqua')
        self.lbl_Fname.grid(row=0,column=0,padx=5,pady=8)
        self.ent_fname = Entry(self.frame_one, font=('arial', 13, 'bold'), fg='black'
                                  , bg='white')
        self.ent_fname.grid(row=0, column=1, pady=8,padx=7)
        self.lbl_lname = Label(self.frame_one, text=' Lname ', font=('arial', 12,
                                                                   'bold'), bg='black', fg='aqua')
        self.lbl_lname.grid(row=1, column=0, padx=5, pady=8)
        self.ent_lname = Entry(self.frame_one, font=('arial', 13, 'bold'), fg='black'
                               , bg='white')
        self.ent_lname.grid(row=1, column=1, pady=8, padx=7)
        self.lbl_address = Label(self.frame_one, text='Address', font=('arial', 12,
                                                                   'bold'), bg='black', fg='aqua')
        self.lbl_address.grid(row=2, column=0, padx=5, pady=8)
        self.ent_address = Entry(self.frame_one, font=('arial', 13, 'bold'), fg='black'
                               , bg='white')
        self.ent_address.grid(row=2, column=1, pady=8, padx=7)
        self.lbl_contact = Label(self.frame_one, text='Contact ', font=('arial', 12,
                                                                     'bold'), bg='black', fg='aqua')
        self.lbl_contact.grid(row=3, column=0, padx=5, pady=8)
        self.ent_contact = Entry(self.frame_one, font=('arial', 13, 'bold'), fg='black'
                                 , bg='white')
        self.ent_contact.grid(row=3, column=1, pady=8, padx=7)
        self.lbl_email = Label(self.frame_one, text='  E-mail  ', font=('arial', 12,
                                                                        'bold'), bg='black', fg='aqua')
        self.lbl_email.grid(row=4, column=0, padx=5, pady=8)
        self.ent_email = Entry(self.frame_one, font=('arial', 13, 'bold'), fg='black'
                                 , bg='white')
        self.ent_email.grid(row=4, column=1, pady=8, padx=7)
        self.lbl_usrname = Label(self.frame_one, text='Username', font=('arial', 11,
                                                                        'bold'), bg='black', fg='aqua')
        self.lbl_usrname.grid(row=5, column=0, padx=5, pady=8)
        self.ent_usrname = Entry(self.frame_one, font=('arial', 13, 'bold'), fg='black'
                               , bg='white')
        self.ent_usrname.grid(row=5, column=1, pady=8, padx=7)
        self.lbl_passwrd= Label(self.frame_one, text='Password', font=('arial', 11,
                                                                        'bold'), bg='black', fg='aqua')
        self.lbl_passwrd.grid(row=6, column=0, padx=5, pady=8)
        self.ent_passwrd = Entry(self.frame_one, font=('arial', 13, 'bold'), fg='black',show='*'
                                 , bg='white')
        self.ent_passwrd.grid(row=6, column=1, pady=8, padx=7)

        #button
        self.btn_reg=Button(self.wn,text='Register',bd=5,activebackground='green',font=('arial',11,'bold')
                            ,bg='cyan',command=self.signin)
        self.btn_reg.place(x=260,y=365)
        self.btn_resett = Button(self.wn, text='  Reset  ', bd=5, activebackground='green', font=('arial', 11, 'bold')
                              , bg='cyan',command=self.resett)
        self.btn_resett.place(x=350, y=365)

    def resett(self):
        self.ent_fname.delete(0,END)
        self.ent_lname.delete(0, END)
        self.ent_address.delete(0, END)
        self.ent_contact.delete(0, END)
        self.ent_email.delete(0, END)
        self.ent_usrname.delete(0, END)
        self.ent_passwrd.delete(0, END)
    def insert(self):
        global d
        le=os.path.getsize("C:\\python danphe\\front_end\\xyz.txt")
        username=self.ent_usrname.get()
        password=self.ent_passwrd.get()
        fname =self.ent_fname.get()
        lname=self.ent_lname.get()
        email = self.ent_email.get()
        contact= self.ent_contact.get()
        address = self.ent_address.get()

        di={username: [password, fname,lname,email,contact,address]}

        if le > 0:
            f=open("xyz.txt","rb+")
            d=pickle.load(f)
            d.update(di)
            f.seek(0)
            pickle.dump(d,f)
            tkinter.messagebox.showinfo("success","Data saved successfully")
            f.close()
            self.wn.destroy()

        else:
            f=open("xyz.txt","wb")
            d.update(di)
            pickle.dump(d,f)
            tkinter.messagebox.showinfo("success", "Data saved successfully")
            f.close()
            self.wn.destroy()
    def signin(self):
        if self.ent_fname.get()=='' and self.ent_lname.get()=='' and self.ent_address.get()=='' and self.ent_usrname.get()=='' \
                and self.ent_passwrd.get()=='':
            tkinter.messagebox.showerror('Error','Please fill up all field')
        else:
            self.insert()


# wn=Tk()
# register_form(wn)
# wn.mainloop()