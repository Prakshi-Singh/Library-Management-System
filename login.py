import tkinter
from tkinter import *
from tkinter import messagebox
import sys
import os
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk
py=sys.executable

class Lib(Tk):
    def __init__(self):
        super().__init__()
        self.a = StringVar()
        self.b = StringVar()
        self.maxsize(1200, 690)
        self.minsize(1200, 690)
        p1 = PhotoImage(file = r'login_logo.png')
        self.iconphoto(False, p1)
        #self.configure(bg="brown")
        self.title("LIBRARY MANAGEMENT SYSTEM")
        
        def chex():
                if len(self.user_text.get()) < 0:
                    messagebox.showinfo(" INVALID LOGIN ID OR PASSWORD!" ,"Try again with valid login!")
                elif len(self.pass_text.get()) < 0: 
                    messagebox.showinfo(" INVALID LOGIN ID OR PASSWORD!","Try again with valid login!")
                else:
                    try:
                        conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                        cursor = conn.cursor()
                        login_id = self.user_text.get()
                        password = self.pass_text.get()
                        cursor.execute('Select * from authentication where login_id= %s AND password = %s ',(login_id,password,))
                        pc = cursor.fetchone()
                        if pc:
                            self.destroy()
                            os.system('%s %s' % (py, 'options.py'))
                        else:
                            print(pc)
                            messagebox.showinfo('ERROR', 'Login id and password not found!')
                            x = messagebox.askyesno("CONFIRMATION","Do you want to register a Staff?")
                            if x:
                                os.system('%s %s' % (py, 'reg.py'))
                            self.user_text.delete(0, END)
                            self.pass_text.delete(0, END)
                    except Error:
                        messagebox.showinfo('ERROR',"Something Went Wrong,Try restarting!")
        def check():
                    image1 = Image.open(r"lib.jpg")
                    image2 = image1.resize((1200, 700), Image.ANTIALIAS)
                    test = ImageTk.PhotoImage(image2)
                    label1 =tkinter.Label(image=test)
                    label1.image = test
                    label1.place(x=0, y=0)
                    self.label = Label(self, text="LOGIN", bg='black', fg='white',font=("times roman", 24,'bold'))
                    self.label.place(x=550, y=90)
                    self.label1 = Label(self, text="LOGIN ID:" ,bg='brown', fg='white', font=("times roman", 18, 'bold'))
                    self.label1.place(x=355, y=180)
                    self.user_text = Entry(self, textvariable=self.a, width=50)
                    self.user_text.place(x=490, y=188)
                    self.label2 = Label(self, text="PASSWORD:" , bg='brown', fg='white',font=("times roman", 18, 'bold'))
                    self.label2.place(x=325, y=248)
                    self.pass_text = Entry(self, show='*', textvariable=self.b, width=50)
                    self.pass_text.place(x=490, y=255)
                    self.butt = Button(self, text="LOGIN" ,bg='black', fg='white', font=12, width=15, command=chex).place(x=530, y=350)
                    self.label3 = Label(self, text="LIBRARY MANAGEMENT SYSTEM",bg='black', fg='white', font=("times roman", 24, 'bold'))
                    self.label3.place(x=350, y=30)
        
        check()
Lib().mainloop()