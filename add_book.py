import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import os
import sys
from PIL import Image, ImageTk
py = sys.executable

#creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        #self.iconbitmap(r'libico.ico')
        self.maxsize(900,600)
        self.minsize(900,600)
        p1 = PhotoImage(file = r'book_logo.png')
        self.iconphoto(False, p1)
        self.title('ADD NEW BOOK')
        self.canvas = Canvas(width=900, height=600)
        self.canvas.pack()
        a = StringVar()
        b = StringVar()
        c = StringVar()
        d = StringVar()
        e = StringVar()
        f = StringVar()
        p = StringVar()
        h = StringVar()
        i = StringVar()
        #verifying Input
        def b_q():
            if len(b.get()) < 1 or len(c.get()) < 1 or len(d.get()) < 1 or len(e.get()) < 1 or len(f.get()) < 1 :
               messagebox.showinfo("ERROR", "Please Enter all details!")
            else:
                g = 'YES'
                #a='null'
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("INSERT INTO books(isbn,title,auth_name,edition,category,price) VALUES (%s,%s,%s,%s,%s,%s) ",(a.get(),b.get(),c.get(),d.get(),e.get(),f.get()))
                    self.conn.commit()
                    self.myCursor.execute("INSERT INTO publisher(publisher_id,pub_year,name,isbn) VALUES (%s,%s,%s,%s) ",(p.get(),i.get(),h.get(),a.get()))
                    self.conn.commit()
                    messagebox.showinfo('INFORMATION', 'Succesfully Added!')
                    ask = messagebox.askyesno("CONFIRMATION", "Do you want to add another book?")
                    if ask:
                        self.destroy()
                        os.system('%s %s' % (py, 'add_book.py'))
                    else:
                        self.destroy()
                except Error:
                    messagebox.showerror("ERROR","Check The Details!")
        #creating input box and label
        image1 = Image.open(r"books.jpg")
        image2 = image1.resize((900, 600), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image2)
        label1 =tkinter.Label(image=test)
        label1.image = test
        label1.place(x=0,y=0)
        Label(self, text='BOOK DETAILS',fg='white',bg='black',font=('times roman', 24, 'bold')).place(x=350,y=30)
        Label(self, text='BOOK ID:',fg='light blue',bg='black', font=('times roman', 15, 'bold')).place(x=240, y=110)
        Entry(self, textvariable=a, width=30).place(x=450, y=113)
        Label(self, text='BOOK TITLE:',fg='light blue',bg='black', font=('times roman', 15, 'bold')).place(x=240, y=150)
        Entry(self, textvariable=b, width=30).place(x=450, y=153)
        Label(self, text='BOOK AUTHOR:',fg='light blue',bg='black', font=('times roman', 15, 'bold')).place(x=240, y=190)
        Entry(self, textvariable=c, width=30).place(x=450, y=193)
        Label(self, text='BOOK EDITION:',fg='light blue',bg='black', font=('times roman', 15, 'bold')).place(x=240, y=230)
        Entry(self, textvariable=d, width=30).place(x=450, y=233)
        Label(self, text='BOOK CATEGORY:',fg='light blue',bg='black', font=('times roman', 15, 'bold')).place(x=240, y=270)
        Entry(self, textvariable=e, width=30).place(x=450, y=273)
        Label(self, text='BOOK PRICE:',fg='light blue',bg='black', font=('times roman', 15, 'bold')).place(x=240, y=310)
        Entry(self, textvariable=f, width=30).place(x=450, y=313)
        Label(self, text='PUBLISHER ID:',fg='light blue',bg='black', font=('times roman', 15, 'bold')).place(x=240, y=350)
        Entry(self, textvariable=p, width=30).place(x=450, y=353)
        Label(self, text='PUBLISHER NAME:',fg='light blue',bg='black', font=('times roman', 15, 'bold')).place(x=240, y=390)
        Entry(self, textvariable=h, width=30).place(x=450, y=393)
        Label(self, text='PUBLICATION YEAR:',fg='light blue',bg='black', font=('times roman', 15, 'bold')).place(x=240, y=430)
        Entry(self, textvariable=i, width=30).place(x=450, y=433)
        Button(self, text="SUBMIT",bg='black', fg='white', font=12, width=8, command=b_q).place(x=400, y=480)
Add().mainloop()