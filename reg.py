from tkinter import *
from tkinter import messagebox
import re
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import os,sys
from PIL import Image, ImageTk
import tkinter
py=sys.executable

#creating window
class reg(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(900, 600)
        self.minsize(900, 600)
        p1 = PhotoImage(file = r'staff_logo.png')
        self.iconphoto(False, p1)
        self.title('LIBRARY ADMINISTRATION')
        self.canvas = Canvas(width=900, height=600)
        self.canvas.pack()
        
#creating variables Please chech carefully
        u = StringVar()
        v = StringVar()
        w= StringVar()
        x= StringVar()
        u='null'
    
        def insert_value():
            try:
                self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                self.myCursor = self.conn.cursor()
                sql="INSERT into authentication(login_id,password) VALUES (%s,%s)"
                values=(w.get(),x.get())
                self.myCursor.execute(sql,values)
                self.myCursor.execute("INSERT into staff(staff_id,name,login_id) VALUES (%s,%s,%s)",(u,v.get(),w.get()))
                self.conn.commit()
                messagebox.showinfo("DONE", "Login Inserted Successfully")
                ask = messagebox.askyesno("CONFIRMATION", "Do you want to add another Login?")
                if ask:
                    self.destroy()
                    os.system('%s %s' % (py, 'reg.py'))
                else:
                    self.destroy()
                    self.myCursor.close()
                    self.conn.close()
            except Error:
                messagebox.showinfo("ERROR", "Something Went Wrong!")
                
#label and input
        image1 = Image.open(r"staff.jpg")
        image2 = image1.resize((900, 600), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image2)
        label1 =tkinter.Label(image=test)
        label1.image = test
        label1.place(x=0,y=0)    
        Label(self, text='LOGIN DETAILS', bg='black', fg='white', font=('times roman', 24, 'bold')).place(x=330, y=120)
        #Label(self, text='STAFF ID:', fg='light blue',bg='black', font=('times roman', 15, 'bold')).place(x=200, y=210)
        #Entry(self, textvariable=u, width=30).place(x=400, y=210)
        Label(self, text='STAFF NAME:', fg='light blue',bg='black', font=('times roman', 15, 'bold')).place(x=200, y=250)
        Entry(self, textvariable=v, width=30).place(x=400, y=250)
        Label(self, text='LOGIN ID:',fg='light blue',bg='black', font=('times roman', 15, 'bold')).place(x=200, y=290)
        Entry(self, textvariable=w, width=30).place(x=400, y=290)
        Label(self, text='PASSWORD:', fg='light blue',bg='black', font=('times roman', 15, 'bold')).place(x=200, y=330)
        Entry(self, textvariable=x, width=30).place(x=400, y=330)
        Button(self, text="SUBMIT", bg='black',fg='white',width=15,font=('TIMES ROMAN', 12), command=insert_value).place(x=350, y=440)
        
reg().mainloop()