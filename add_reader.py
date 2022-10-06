from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter
import os
import sys
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk
py = sys.executable

#creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(900,600)
        self.minsize(900,600)
        p1 = PhotoImage(file = r'reader_logo.png')
        self.iconphoto(False, p1)
        self.title('ADD NEW READER')
        self.canvas = Canvas(width=900, height=600)
        self.canvas.pack()
        a = StringVar()
        b = StringVar()
        c = StringVar()
        d = StringVar()
        e = StringVar()
        f = StringVar()
        a='null'
        
#verifying input
        def asi():
            if len(b.get()) < 1:            
                messagebox.showinfo("Oop's", "Please Enter Email Id")
            elif len(c.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Name")
            elif len(d.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Phone Number")
            elif len(e.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Address")
            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='library',
                                                        user='root',
                                                        password='')
                    self.myCursor = self.conn.cursor()
                    #id = a.get()
                    eid=b.get()
                    name=c.get()
                    pno=d.get()
                    add=e.get()
                    sid=f.get()
                    '''sql="Insert into readers(user_id, email,name,phone_no,address,staff_id) values (%s,%s,%s,%s,%s,%s)"
                    values=(id,eid,name,pno,add,sid,sql,)'''
                    self.myCursor.execute("Insert into readers(user_id, email,name,phone_no,address) values (%s,%s,%s,%s,%s)",(a,b.get(),c.get(),d.get(),e.get()))
                    self.conn.commit()
                    messagebox.showinfo("DONE","Reader Inserted Successfully!")
                    ask = messagebox.askyesno("CONFIRMATION","Do you want to add another reader?")
                    if ask:
                     self.destroy()
                     os.system('%s %s' % (py, 'add_reader.py'))
                    else:
                     self.destroy()
                     self.myCursor.close()
                     self.conn.close()
                except Error:
                    messagebox.showerror("ERROR","Something Went Wrong!")

        # label and input box
        image1 = Image.open(r"reader.jpg")
        image2 = image1.resize((900, 600), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image2)
        label1 =tkinter.Label(image=test)
        label1.image = test
        label1.place(x=0,y=0)
        Label(self, text='READER DETAILS',fg='White',bg='black', font=('times roman', 24, 'bold')).place(x=315,y=80)
        #Label(self, text='USER ID:',fg='light blue',bg='black', font=('times roman', 15, 'bold')).place(x=250, y=170)
        #Entry(self, textvariable=a, width=30).place(x=440, y=170)
        Label(self, text='EMAIL ID:',fg='light blue',bg='black', font=('times roman', 15, 'bold')).place(x=250, y=210)
        Entry(self, textvariable=b, width=30).place(x=440, y=210)
        Label(self, text='NAME:',fg='light blue',bg='black', font=('times roman', 15, 'bold')).place(x=250, y=250)
        Entry(self, textvariable=c, width=30).place(x=440, y=250)
        Label(self, text='PHONE NUMBER:',fg='light blue',bg='black', font=('times roman', 15, 'bold')).place(x=250, y=290)
        Entry(self, textvariable=d, width=30).place(x=440, y=290)
        Label(self, text='ADDRESS:',fg='light blue',bg='black', font=('times roman', 15, 'bold')).place(x=250, y=330)
        Entry(self, textvariable=e,width=50).place(x=440, y=330)
        '''Label(self, text='Staff Id:',bg='light blue', font=('Courier new', 10, 'bold')).place(x=70, y=280)
        Entry(self, textvariable=f, width=30).place(x=200, y=280)'''
        Button(self, text="SUBMIT",bg='black', fg='white',font=12,width = 15,command=asi).place(x=350, y=430)

Add().mainloop()

'''elif len(f.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Your Staff Id")'''