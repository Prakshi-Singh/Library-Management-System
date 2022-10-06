from datetime import date, datetime
from tkinter import *
import tkinter
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk
import os
import sys
py = sys.executable

#creating window
class issue(Tk):
    def __init__(self):
        super().__init__()
        self.title('LIBRARY ADMINISTRATION')
        self.maxsize(900,600)
        p1 = PhotoImage(file = r'book_logo.png')
        self.iconphoto(False, p1)
        self.canvas = Canvas(width=900, height=600)
        self.canvas.pack()
        a = StringVar()
        b = StringVar()
        c = StringVar()
        
        d = StringVar()
        e = StringVar()

#verifying input
        def isb():
            if (len(a.get())) == 0 or (len(b.get())) == 0 or (len(c.get())) == 0:
                messagebox.showinfo('ERROR', 'Empty field!')
            else:
             try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='library',
                                                        user='root',
                                                        password='')
                    z=0
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("SELECT isbn from books where user_id=%s and staff_id=%s and isbn= %s",(z,z,b.get(),))
                    self.pc = self.mycursor.fetchall()
                    try:
                     if self.pc:
                        print("success")
                        now = datetime.now()
                        idate = now.strftime('%Y-%m-%d %H:%M:%S')
                        z=0
                        self.mycursor.execute("INSERT INTO return_b(reserve_id,issue_date,user_id,staff_id,isbn) VALUES (%s,%s,%s,%s,%s)",(e.get(),idate,c.get(),a.get(),b.get(),))
                        self.conn.commit()
                        self.mycursor.execute("UPDATE readers SET staff_id=%s WHERE  user_id= %s",(a.get(),c.get(),))
                        self.conn.commit()
                        self.mycursor.execute("UPDATE books SET staff_id=%s , user_id=%s WHERE  isbn= %s",(a.get(),c.get(),b.get(),))
                        self.conn.commit()
                        messagebox.showinfo("SUCCESS", "Successfully Issued!")
                        ask = messagebox.askyesno("CONFIRMATION", "Do you want to issue another?")
                        if ask:
                            self.destroy()
                            os.system('%s %s' % (py, 'issue_book.py'))
                        else:
                            self.destroy()
                     else:
                        messagebox.showinfo("Oop's", "Book id "+b.get()+" is not available!")
                    except Error:
                        messagebox.showerror("ERROR", "Check The Details!")
             except Error:
                    messagebox.showerror("ERROR", "Something Went Wrong!")
                    
#label and input box
        image1 = Image.open(r"books.jpg")
        image2 = image1.resize((900, 600), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image2)
        label1 =tkinter.Label(image=test)
        label1.image = test
        label1.place(x=0,y=0)
        Label(self, text='BOOK ISSUING',fg='white',bg='black', font=('Times roman', 24,'bold')).place(x=350, y=120)
        #Label(self, text='REG ID:',fg='light blue',bg='black', font=('times roman', 15, 'bold')).place(x=250, y=230)
        #Entry(self, textvariable=e, width=40).place(x=400, y=230)
        Label(self, text='STAFF ID:',fg='light blue',bg='black', font=('Times roman', 15,'bold')).place(x=250, y=270)
        Entry(self, textvariable=a, width=40).place(x=400, y=270)
        Label(self, text='BOOK ID:',fg='light blue',bg='black', font=('Times roman', 15,'bold')).place(x=250, y=310)
        Entry(self, textvariable=b, width=40).place(x=400, y=310)
        Label(self, text='READER ID:',fg='light blue',bg='black', font=('Times roman', 15,'bold')).place(x=250, y=350)
        Entry(self, textvariable=c, width=40).place(x=400, y=350)
        Button(self, text="ISSUE", bg='black', fg='white', font=12,width=15, command=isb).place(x=350, y=450)
        
issue().mainloop()
