from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
from PIL import ImageTk,Image
import os,glob
import mysql.connector
from PIL import Image, ImageTk
from mysql.connector import Error

class Search(Tk):
    def __init__(self):
        super().__init__()
        f = StringVar()
        g = StringVar()
        self.title("SEARCHING READER INFORMATION")
        self.maxsize(900,600)
        self.minsize(900,600)
        p1 = PhotoImage(file = r'reader_logo.png')
        self.iconphoto(False, p1)
        self.canvas = Canvas(width=900, height=600)
        self.canvas.pack()
        image1 = Image.open(r"reader.jpg")
        image2 = image1.resize((900, 600), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image2)
        label1 =tkinter.Label(image=test)
        label1.image = test
        label1.place(x=0,y=0)
        l1=Label(self,text="SEARCH READER",fg='white',bg='black', font=("TIMES ROMAN",24,'bold')).place(x=300,y=20)
        l = Label(self, text="SEARCH BY:",fg='light blue',bg='black', font=("TIMES ROMAN", 15, 'bold')).place(x=95, y=96)


        def ge():
            if (len(self.combo.get())) == 0:
                messagebox.showinfo('ERROR', 'First enter the value!')
            elif (len(self.entry.get())) == 0:
                messagebox.showinfo('ERROR', 'Enter the '+self.combo.get())
            elif self.combo.get() == 'Name':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                    self.mycursor = self.conn.cursor()
                    name = self.entry.get()
                    self.mycursor.execute("SELECT * from readers where name like %s",('%'+name+'%',))
                    pc = self.mycursor.fetchall()
                    if pc:
                        self.listTree.delete(*self.listTree.get_children())
                        for row in pc:
                            cpt = 0
                            self.listTree.insert("",'end',text=str(row[cpt]) ,values=(row[1], row[2], row[3],row[4]))
                            cpt += 1
                    else:
                        messagebox.showinfo("OOP'S","Name not found!")
                except Error:
                    messagebox.showerror("ERROR", "Something Went Wrong!")
            elif self.combo.get() == 'ID':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                    
                    self.mycursor = self.conn.cursor()
                    id = int(self.entry.get())
                    self.mycursor.execute("SELECT * from readers where user_id=%s", (id,))
                    pc = self.mycursor.fetchall()
                    if pc:
                        for row in pc:
                            cpt = 0
                            self.listTree.insert("",'end',text=str(row[cpt]) ,values=(row[1], row[2], row[3],row[4]))
                            cpt += 1
                    else:
                        messagebox.showinfo("OOP'S", "ID not found!")
                except Error:
                    messagebox.showerror("ERROR", "Something Went Wrong!")

        
        self.b= Button(self,text="FIND",bg='black', fg='white',width=15,font=("TIMES ROMAN",12,'bold'),command= ge )
        self.b.place(x=510,y=148)
        self.combo=ttk.Combobox(self,textvariable=g,values=("Name","ID"),width=40,state="readonly")
        self.combo.place(x = 230, y = 100)
        self.entry = Entry(self,textvariable=f,width=43)
        self.entry.place(x=230,y=155)
        self.la = Label(self, text="ENTER:",fg='LIGHT BLUE',bg='black', font=("times roman", 15, 'bold')).place(x=140, y=150)

        def handle(event):
            if self.listTree.identify_region(event.x,event.y) == "separator":
                return "break"


        self.listTree = ttk.Treeview(self, height=13,columns=('Email','Reader Name', 'Phone Number', 'Address'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.listTree.configure(yscrollcommand=self.vsb.set)
        self.listTree.heading("#0", text='READER ID', anchor='w')
        self.listTree.column("#0", width=75, anchor='w')
        self.listTree.heading("Email", text='EMAIL')
        self.listTree.column("Email", width=125, anchor='center')        
        self.listTree.heading("Reader Name", text='NAME')
        self.listTree.column("Reader Name", width=150, anchor='center')
        self.listTree.heading("Phone Number", text='PHONE NUMBER')
        self.listTree.column("Phone Number", width=120, anchor='center')
        self.listTree.heading("Address", text='ADDRESS')
        self.listTree.column("Address", width=175, anchor='center')
        self.listTree.place(x=110, y=230)
        self.vsb.place(x=738,y=231,height=285)
        ttk.Style().configure("Treeview", font=('Times new Roman', 10))

Search().mainloop()