import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
from mysql.connector import Error
#creating widow
class Rer(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(900, 600)
        self.minsize(900, 600)
        self.title("REMOVING BOOK")
        p1 = PhotoImage(file = r'book_logo.png')
        self.iconphoto(False, p1)
        self.canvas = Canvas(width=1366, height=768)
        self.canvas.pack()
        a = StringVar()
        def ent():
            if len(a.get()) ==0:
                messagebox.showinfo("ERROR","Please Enter A Valid Id!")
            else:
                d = messagebox.askyesno("CONFIRMATION", "Are you sure you want to remove book?")
                if d:
                    try:
                        self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                        self.myCursor = self.conn.cursor()
                        z=0
                        self.myCursor.execute("DELETE from books where isbn = %s",(a.get(),))
                        self.conn.commit()
                        self.myCursor.execute("DELETE from publisher where isbn = %s",(a.get(),))
                        self.conn.commit()
                        self.conn.close()
                        messagebox.showinfo("CONFIRMATION","Book Removed Successfully!")
                        a.set("")
                    except:
                        messagebox.showerror("ERROR","Something Went Wrong!")
        image1 = Image.open(r"books.jpg")
        image2 = image1.resize((900, 600), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image2)
        label1 =tkinter.Label(image=test)
        label1.image = test
        label1.place(x=0,y=0) 
        Label(self, text='REMOVING BOOK',fg='white',bg='black',font=('times roman', 24, 'bold')).place(x=350,y=40)               
        Label(self, text = "ENTER BOOK ID: ",fg='light blue',bg='black', font=('times roman', 15, 'bold')).place(x=215, y=240)
        Entry(self,textvariable = a,width = 37).place(x = 410,y = 245)
        Button(self, text='REMOVE', bg='black', fg='white',width=15, font=('TIMES ROMAN', 12),command = ent).place(x=400, y = 400)

Rer().mainloop()