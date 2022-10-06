from tkinter import *
from tkinter import messagebox
import tkinter
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk
#creating widow
class Rem(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(900, 600)
        self.minsize(900, 600)
        p1 = PhotoImage(file = r'staff_logo.png')
        self.iconphoto(False, p1)
        self.title("LIBRARY ADMINISTRATION")
        self.canvas = Canvas(width=900, height=600)
        self.canvas.pack()
        a = StringVar()
        def ent():
            if len(a.get()) ==0:
                messagebox.showinfo("ERROR","Please Enter A Valid Id!")
            else:
                d = messagebox.askyesno("CONFIRMATION", "Are you sure you want to remove the staff?")
                if d:
                    try:
                        self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                        self.myCursor = self.conn.cursor()
                        self.myCursor.execute("Delete from authentication where login_id = %s",(a.get(),))
                        self.conn.commit()
                        self.myCursor.execute("Delete from staff where login_id = %s",(a.get(),))
                        self.conn.commit()
                        self.myCursor.close()
                        self.conn.close()
                        messagebox.showinfo("CONFIRMATION","Staff Removed Successfully!")
                        a.set("")
                    except:
                        messagebox.showerror("ERROR","Something Went Wrong!")
        image1 = Image.open(r"staff.jpg")
        image2 = image1.resize((900, 600), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image2)
        label1 =tkinter.Label(image=test)
        label1.image = test
        label1.place(x=0,y=0)    
        Label(self, text='REMOVE STAFF',fg='white',bg='black', font=('times roman', 24, 'bold')).place(x=330,y=120)             
        Label(self, text = "ENTER LOGIN ID: ",fg='light blue',bg='black',font=('TIMES ROMAN', 15, 'bold')).place(x=230,y =280)
        Entry(self,textvariable = a,width = 37).place(x = 420,y = 285)
        Button(self, text='REMOVE',bg='black', fg='white', width=15, font=('TIMES ROMAN', 12),command = ent).place(x=350, y = 430)

Rem().mainloop()