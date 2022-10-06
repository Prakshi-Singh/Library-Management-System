import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import os
import sys
from PIL import Image, ImageTk
py = sys.executable


class Search(Tk):
    def __init__(self):
        super().__init__()
        f = StringVar()
        g = StringVar()
        self.title("SEARCHING BOOK INFORMATION")
        self.maxsize(900,600)
        self.minsize(900,600)
        p1 = PhotoImage(file = r'book_logo.png')
        self.iconphoto(False, p1)
        self.canvas = Canvas(width=900, height=600)
        self.canvas.pack()
        image1 = Image.open(r"books.jpg")
        image2 = image1.resize((900, 600), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image2)
        label1 =tkinter.Label(image=test)
        label1.image = test
        label1.place(x=0,y=0)
        l1=Label(self,text="SEARCH LIBRARY",fg='white',bg='black', font=("times roman",24,'bold')).place(x=330,y=20)
        l = Label(self, text="SEARCH BY:",fg='light blue',bg='black', font=("times roman", 15, 'bold')).place(x=95, y=96)
        
        def insert(data):
            self.listTree.delete(*self.listTree.get_children())
            for row in data:
                cpt = 0
                self.listTree.insert("",'end',text=str(row[cpt]) ,values=(row[1], row[2], row[3],row[4],row[5]))
                cpt += 1
                            
        def ge():
            if (len(g.get())) == 0:
                messagebox.showinfo('ERROR', 'First choose the value!')
            elif (len(f.get())) == 0:
                messagebox.showinfo('ERROR', 'Enter the '+g.get())
            elif g.get() == 'Book Name':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("SELECT isbn,title,auth_name,edition,category,price from books where title like %s",('%'+f.get()+'%',))
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        self.listTree.delete(*self.listTree.get_children())
                        for row in self.pc:
                            insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Either Book Name is incorrect or it is not available!")
                except Error:
                    messagebox.showerror("ERROR","Something Went Wrong!")
            elif g.get() == 'Author Name':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("SELECT isbn,title,auth_name,edition,category,price from books where auth_name like %s",('%'+f.get()+'%',))
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Author not found!")
                except Error:
                    messagebox.showerror("ERROR","Something Went Wrong!")
            elif g.get() == 'Category':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("SELECT isbn,title,auth_name,edition,category,price from books where category like %s", ('%'+f.get()+'%',))
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","No book is avaiable on this category!")
                except Error:
                    messagebox.showerror("ERROR","Something Went Wrong!")
                    
        b=Button(self,text="FIND",bg='black', fg='white',width=15,font=("times roman",12,'bold'),command=ge).place(x=510,y=148)
        c=ttk.Combobox(self,textvariable=g,values=("Book Name","Author Name","Category"),width=40,state="readonly").place(x = 230, y = 100)
        en = Entry(self,textvariable=f,width=43).place(x=230,y=155)
        la = Label(self, text="ENTER:",fg='LIGHT BLUE',bg='black', font=("times roman", 15, 'bold')).place(x=140, y=150)

        def handle(event):
            if self.listTree.identify_region(event.x,event.y) == "separator":
                return "break"


        self.listTree = ttk.Treeview(self, height=13,columns=('Book Name', 'Book Author', 'Edition','Category','price'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.listTree.configure(yscrollcommand=self.vsb.set)
        self.listTree.heading("#0", text='BOOK ID', anchor='center')
        self.listTree.column("#0", width=85, anchor='center')
        self.listTree.heading("Book Name", text='BOOK NAME')
        self.listTree.column("Book Name", width=200, anchor='center')
        self.listTree.heading("Book Author", text='BOOK AUTHOR')
        self.listTree.column("Book Author", width=150, anchor='center')
        self.listTree.heading("Edition", text='EDITION')
        self.listTree.column("Edition", width=60, anchor='center')
        self.listTree.heading("Category", text='CATEGORY')
        self.listTree.column("Category", width=150, anchor='center')
        self.listTree.heading("price", text='PRICE')
        self.listTree.column("price", width=80, anchor='center')
        self.listTree.bind('&lt;Button-1&gt;', handle)
        self.listTree.place(x=90, y=240)
        self.vsb.place(x=813,y=240,height=287)
        ttk.Style().configure("Treeview", font=('Times new Roman', 10))

Search().mainloop()