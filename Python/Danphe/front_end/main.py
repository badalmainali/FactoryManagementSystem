from tkinter import *
from PIL import ImageTk
import pyttsx3
import front_end.emp
from front_end.emp import *
from front_end.tea_main import *
import front_end.tea_main
from front_end.view_tea import *
import front_end.view_tea


class main_interface():
    def __init__(self,window):
        self.wn=window
        self.wn.geometry('700x550+290+100')
        self.wn.title('Main ')
        self.wn.resizable(False,False)


    #inserting an image background
        self.main_img=ImageTk.PhotoImage(file='images/main.jpg')

        self.factory_img = ImageTk.PhotoImage(file='images/factory.png')
        #
        main_bg=Label(self.wn,image=self.main_img).place(x=0,y=0)
        factory_bg = Label(self.wn, image=self.factory_img).place(x=240,y=60)

        self.heading_lbl=Label(self.wn,text="Danphe Factory",font=('Times',24,'bold'),bg='#c5d0d9')
        self.heading_lbl.pack(side=TOP,fill=X)

    #creating button
        self.btn_employee=Button(self.wn,text='Manage Employee',font=('Goudy old style',16,'bold'),bg='#e2c7eb',bd=2,command=self.employee_call)
        self.btn_employee.place(x=260,y=200)

        self.btn_teas = Button(self.wn, text='Manage Tea leaves', font=('Goudy old style', 16, 'bold'), bg='#e2c7eb', bd=2,command=self.tea_call)
        self.btn_teas.place(x=260, y=270)

        self.btn_protocols = Button(self.wn, text='    View Record     ', font=('Goudy old style', 16, 'bold'),
                                   bg='#e2c7eb', bd=2,command=self.tea_view)
        self.btn_protocols.place(x=260, y=340)
        self.btn_exit = Button(self.wn, text='             Exit           ', font=('Goudy old style', 16, 'bold'),
                                   bg='#e2c7eb', bd=2,command=self.exit)
        self.btn_exit.place(x=260, y=410)


    def exit(self):
        self.wn.destroy()

    def employee_call(self):
        window=Toplevel()
        front_end.emp.Employee(window)

    def tea_call(self):
        win=Toplevel()
        front_end.tea_main.tea_manage(win)



    def tea_view(self):
        windows1 = Toplevel()
        front_end.view_tea.view_info(windows1)






#
# wn=Tk()
# obj=main_interface(wn)
# wn.mainloop()