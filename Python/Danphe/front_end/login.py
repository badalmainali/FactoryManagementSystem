
from tkinter import*
from PIL import ImageTk
import os
import pyttsx3
import tkinter.messagebox
import pickle
from front_end.register import *
import front_end.register
import front_end.main
# from front_end.main import *

class log_in_form:
    def __init__(self,window):
        self.wn=window

        self.wn.title('Login')
        self.wn.geometry('550x400+500+150')
        self.wn.resizable(False,False)
        #image.....................
        self.bg_img=ImageTk.PhotoImage(file='images/mainbg.jpg')
        self.admin_img = ImageTk.PhotoImage(file='images/admin.png')



        bg_label=Label(self.wn,image=self.bg_img).pack()
        admin_label = Label(self.wn, image=self.admin_img).place(x=220,y=30)

       #=====Label=======
        self.lbl_head=Label(self.wn,text='Admin LogIn',bg='black',fg='white'
                            ,font=('arial',14,'bold'),bd=7,relief=GROOVE)
        self.lbl_head.place(x=0,y=0,relwidth=1)

        #creating frame
        self.frame1=Frame(self.wn,bd=3)
        self.frame1.place(x=128,y=160,height=250,width=300)
        #creating label inside frame

        self.lbl_username=Label(self.frame1,text='Username',font=('arial',14,
                                            'bold'),bg='black',fg='aqua')
        self.lbl_username.grid(row=0,column=0,padx=5,pady=8)

        self.lbl_password = Label(self.frame1, text='Password', font=('arial', 14,
                                                                 'bold'), bg='black', fg='aqua')
        self.lbl_password.grid(row=1, column=0, padx=5, pady=8)

        self.lbl_admin_code = Label(self.frame1, text='  Contact  ', font=('arial', 14,
                                                                 'bold'), bg='black', fg='aqua')
        self.lbl_admin_code.grid(row=2, column=0, padx=5, pady=8)

        #creating entries
        self.ent_username=Entry(self.frame1,font=('arial',13,'bold'),fg='black'
                           ,bg='white')
        self.ent_username.grid(row=0, column=1, pady=8)
        self.ent_password = Entry(self.frame1, font=('arial', 13, 'bold'), fg='black',show='*'
                             , bg='white')
        self.ent_password.grid(row=1, column=1, pady=8)
        self.ent_admin_code= Entry(self.frame1, font=('arial', 13, 'bold'), fg='black'
                             , bg='white')
        self.ent_admin_code.grid(row=2, column=1, pady=8)

        #creating buttons
        self.btn_login=Button(self.frame1,text="Login",bd=2,bg='cyan'
                ,fg='black',activebackground='#03fc3d',font=('arial',12,'bold'),command=self.login)
        self.btn_login.place(x=90,y=140)
        self.btn_reset = Button(self.frame1, text="Reset", bd=2, bg='cyan'
                           , fg='black', activebackground='#03fc3d', font=('arial', 12, 'bold'),command=self.reset_value)
        self.btn_reset.place(x=160, y=140)
        self.btn_register = Button(self.frame1, text="Register", bd=2, bg='cyan'
                           , fg='black', activebackground='#03fc3d', font=('arial', 12, 'bold'),command=self.register_btn)
        self.btn_register.place(x=180, y=180)

        self.note_lbl=Label(self.frame1,text='Newly assigned Admin?',font=('arial',10,'italic'),fg='black')
        self.note_lbl.place(x=30,y=186)


    def reset_value(self):
        self.ent_username.delete(0,END)
        self.ent_password.delete(0,END)
        self.ent_admin_code.delete(0,END)

    def login(self):

        if self.ent_password.get() == '' or self.ent_username.get() == '' or self.ent_admin_code=='':
            tkinter.messagebox.showerror('Error', 'Please fill up')

        else:
            self.load()
    def load(self):
        le = os.path.getsize("C:\\python danphe\\front_end\\xyz.txt")

        if le > 0:
            f = open("xyz.txt", "rb+")
            ld = pickle.load(f)
            f.close()
            for i, j in ld.items():
                if i == self.ent_username.get():
                    for p in j:
                        if self.ent_password.get() == p:

                            tkinter.messagebox.showinfo(f'Hey {self.ent_username.get()}!', "Login Successful")

                            self.txtSpeech()
                            self.wn.destroy()
                            self.call()
                            return
            else:
                tkinter.messagebox.showerror("Sign Up First", "Wrong Password or Username")
                f.close()
        else:
            tkinter.messagebox.showerror("Sign Up First", "Please register First")




    def register_btn(self):
        window=Toplevel()
        front_end.register.register_form(window)

    def call(self):
        window_new=Tk()
        front_end.main.main_interface(window_new)

    def txtSpeech(self):
        eng=pyttsx3.init()
        eng.say(f'congratulations {self.ent_username.get()} ,you are logged in')
        eng.runAndWait()










wn=Tk()
log_in_form(wn)
wn.mainloop()