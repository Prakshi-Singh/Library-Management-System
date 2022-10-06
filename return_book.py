import tkinter
from tkinter import *
from tkinter import messagebox
import os,sys
import mysql.connector
from mysql.connector import Error
from datetime import datetime,date
from PIL import Image, ImageTk
py = sys.executable


class ret(Tk):
    def __init__(self):
        super().__init__()
        self.title("BOOK RETURNING")
        self.maxsize(900,600)
        p1 = PhotoImage(file = r'book_logo.png')
        self.iconphoto(False, p1)
        self.canvas = Canvas(width=900, height=600)
        self.canvas.pack()
        self.cal = 0
        a = StringVar()

        def qui():
            if len(a.get()) == '0':
                messagebox.showerror("ERROR","Please Enter The Book Id!")
            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='library',
                                                        user='root',
                                                        password='')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("SELECT isbn from return_b where return_date is null and isbn=%s",(a.get(),))
                    temp = self.mycursor.fetchone()
                    if temp:
                        z=0
                        self.mycursor.execute("UPDATE books SET staff_id=%s , user_id=%s WHERE  isbn= %s",(z,z,a.get()))
                        self.conn.commit()
                        now = datetime.now()
                        idate = now.strftime('%Y-%m-%d %H:%M:%S')
                        self.mycursor.execute("UPDATE return_b set return_date = %s where isbn = %s",(idate,a.get(),))
                        self.conn.commit()
                        self.conn.close()
                        messagebox.showinfo('SUCCESS', 'Succesfully Returned!')
                        d = messagebox.askyesno("CONFIRMATION", "Return more books?")
                        if d:
                            self.destroy()
                            os.system('%s %s' % (py, 'return_book.py'))
                        else:
                            self.destroy()
                    else:
                        messagebox.showinfo("Oop's", "Book not yet issued!")
                except Error:
                    messagebox.showerror("ERROR","Something Went Wrong!")
        image1 = Image.open(r"books.jpg")
        image2 = image1.resize((900, 600), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image2)
        label1 =tkinter.Label(image=test)
        label1.image = test
        label1.place(x=0,y=0)            
        Label(self, text='RETURN BOOK',fg='white',bg='black', font=('Times roman', 24,'bold')).place(x=350, y=120)
        Label(self, text='ENTER BOOK ID:',fg='light blue',bg='black', font=('TIMES ROMAN', 15, 'bold')).place(x=200, y=300)
        Entry(self, textvariable=a, width=40).place(x=400, y=306)
        Button(self, text="RETURN",bg='black', fg='white', font=12, width=15, command=qui).place(x=350, y=430)
ret().mainloop()