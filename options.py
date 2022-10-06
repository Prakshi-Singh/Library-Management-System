from tkinter import *
from tkinter import messagebox
import os
import sys
from tkinter import ttk
import tkinter
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk
py=sys.executable

#creating window
class MainWin(Tk):
    def __init__(self):
        super().__init__()
        #self.configure(bg='light blue')
        self.canvas = Canvas(width=1320, height=768)
        self.canvas.pack()
        self.maxsize(1320, 768)
        self.minsize(1320,768)
        p1 = PhotoImage(file = r'login_logo.png')
        self.iconphoto(False, p1)
        self.state('zoomed')
        self.title('LIBRARY MANAGEMENT SYSTEM')
        self.a = StringVar()
        self.b = StringVar()
        self.c = StringVar()
        self.mymenu = Menu(self)
#calling scripts
        def a_r():
            os.system('%s %s' % (py, 'add_reader.py')) #done

        def a_b():
            os.system('%s %s' % (py, 'add_book.py')) #done

        def r_b():
            os.system('%s %s' % (py, 'remove_book.py'))

        def r_r():
            os.system('%s %s' % (py, 'remove_reader.py'))#doing

        def ib():
            os.system('%s %s' % (py, 'issue_book.py'))#done

        def ret():
            os.system('%s %s' % (py, 'return_book.py'))#done

        def sea():
            os.system('%s %s' % (py,'search_book.py'))#done

        def log():
            conf = messagebox.askyesno("CONFIRMATION", "Are you sure you want to Logout?")
            if conf:
             self.destroy()
             os.system('%s %s' % (py, 'login.py')) #done



      # def handle(event):
        #     if self.listTree.identify_region(event.x,event.y) == "separator":
        #         return "break"
        def add_user():
            os.system('%s %s' % (py, 'reg.py'))#done
        def rem_user():
            os.system('%s %s' % (py, 'rem_user.py'))#done
        def sest():
            os.system('%s %s' % (py,'search_reader.py'))#done

#creating table

        image1 = Image.open(r"options.jpeg")
        image2 = image1.resize((1320, 768), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image2)
        label1 =tkinter.Label(image=test)
        label1.image = test
        label1.place(x=0, y=0)
        self.listTree = ttk.Treeview(self,height=14,columns=('book_id','book_title','publisher_id','return_date'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.hsb = ttk.Scrollbar(self,orient="horizontal",command=self.listTree.xview)
        self.listTree.configure(yscrollcommand=self.vsb.set,xscrollcommand=self.hsb.set)
        
        self.listTree.heading("#0", text='READER ID')
        self.listTree.column("#0", width=100,minwidth=100,anchor='center')

        self.listTree.heading("book_id", text='BOOK ID')
        self.listTree.column("book_id", width=150, minwidth=150,anchor='center')
        self.listTree.heading("book_title", text='BOOK TITLE')
        self.listTree.column("book_title", width=200, minwidth=200,anchor='center')
        
        self.listTree.heading("publisher_id", text='PUBLISHER ID')
        self.listTree.column("publisher_id", width=125, minwidth=125,anchor='center')
        
        self.listTree.heading("return_date", text='RETURN DATE')
        self.listTree.column("return_date", width=123, minwidth=123, anchor='center')
        '''self.listTree.place(x=200,y=360)
        self.vsb.place(x=1036,y=361,height=305)
        self.hsb.place(x=201,y=650,width=850)'''
        self.listTree.place(x=320,y=360)
        self.vsb.place(x=1020,y=361,height=291)
        self.hsb.place(x=322,y=650,width=705)
        ttk.Style().configure("Treeview",font=('Times new Roman',10))

        list1 = Menu(self)
        list1.add_command(label="Add Reader", command=a_r)
        list1.add_command(label="Add Book", command=a_b)

        list3 = Menu(self)
        list3.add_command(label = "Add Staff",command = add_user)
        list3.add_command(label = "Remove Staff",command = rem_user)
        
        list2 = Menu(self)
        list2.add_command(label = "Remove Reader",command = r_r)
        list2.add_command(label = "Remove Book",command = r_b)


        self.mymenu.add_cascade(label='Add', menu=list1)
        self.mymenu.add_cascade(label = 'Admin Tools', menu = list3)
        self.mymenu.add_cascade(label='Remove',menu=list2)

        self.config(menu=self.mymenu)

        def ser():
            if(len(self.studid.get())==0):
                messagebox.showinfo("ERROR", "Empty Field!")
            else:

             try:
                conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                cursor = conn.cursor()
                #sql="SELECT r.user_id,b.isbn,b.title,p.publisher_id,rd.return_date from books b,readers r,return_b rd,publisher p where b.isbn=rd.isbn and b.user_id=r.user_id and rd.user_id=r.user_id and p.isbn=b.isbn and r.user_id=%s"
                #change = int(self.studid.get())
                #cursor.execute(sql,(change,))
                cursor.callproc('display_readers',(self.studid.get(),))
                for results in cursor.stored_results():
                    pc = results.fetchall()
                    if pc:
                        self.listTree.delete(*self.listTree.get_children())
                        for row in pc:
                            cpt = 0
                            self.listTree.insert("",'end',text=str(row[cpt]) ,values=(row[1], row[2], row[3],row[4]))
                            cpt += 1
                    else:
                        messagebox.showinfo("ERROR", "Please check the ID again or any book is not yet issued on this ID")
             except Error:
                #print(Error)
              messagebox.showerror("ERROR","Something Went Wrong!")
              
        def ent():
            if (len(self.bookid.get()) == 0 or len(self.pubid.get())==0):
                messagebox.showinfo("ERROR", "Empty Field!")
            else:
             try:
                self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                self.myCursor = self.conn.cursor()
                #sql="select r.user_id,b.isbn,b.title,p.publisher_id,rd.return_date from books b,readers r,return_b rd,publisher p where b.isbn=rd.isbn and b.user_id=r.user_id and rd.user_id=r.user_id and p.isbn=b.isbn and b.isbn=%s and p.publisher_id=%s"
                #book=int(self.bookid.get())
                #pub=int(self.pubid.get())
                #values=(book,pub,)
                #self.myCursor.execute(sql,values)
                self.myCursor.callproc('display_books',(self.bookid.get(),self.pubid.get(),))
                for results in self.myCursor.stored_results():
                    self.pc = results.fetchall()
                    if self.pc:
                        self.listTree.delete(*self.listTree.get_children())
                        for row in self.pc:
                            cpt = 0
                            self.listTree.insert("",'end',text=str(row[cpt]) ,values=(row[1], row[2], row[3],row[4]))
                            cpt += 1
                    else:
                        messagebox.showinfo("ERROR", "Please check the ID again or any book is not yet issued on this ID")
             except Error:
                messagebox.showerror("ERROR","Something Went Wrong!")

        def check():
            try:
                conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                mycursor = conn.cursor()
                mycursor.execute("Select * from authentication")
                z = mycursor.fetchone()
                if not z:
                    messagebox.showinfo("ERROR", "Please Register The Staff")
                    x = messagebox.askyesno("CONFIRM","Do you want to register a Staff?")
                    if x:
                        self.destroy()
                        os.system('%s %s' % (py, 'reg.py'))
                else:
                    #label and input box
                    
                    self.label3 = Label(self, text='LIBRARY MANAGEMENT SYSTEM', bg='black', fg='white' ,font=('times roman', 30, 'bold'))
                    self.label3.place(x=350, y=22)
                    self.label4 = Label(self, text="ENTER READER ID",bg='brown', fg='white', font=('times roman', 18, 'bold'))
                    self.label4.place(x=120, y=107)
                    self.studid = Entry(self, textvariable=self.a, width=90)
                    self.studid.place(x=345, y=112)
                    self.srt = Button(self, text='SEARCH',bg='black', fg='white', width=15, font=('times roman', 10),command = ser).place(x=1000, y=106)
                    
                    self.label5 = Label(self, text="BOOK ID",bg='brown', fg='white', font=('times roman', 18, 'bold'))
                    self.label5.place(x=175, y=154)
                    self.bookid = Entry(self, textvariable=self.b, width=30)
                    self.bookid.place(x=290, y=160)
                    self.label6 = Label(self, text="PUBLISHER ID",bg='brown', fg='white', font=('times roman', 18, 'bold'))
                    self.label6.place(x=530, y=154)
                    self.pubid = Entry(self, textvariable=self.c, width=30)
                    self.pubid.place(x=715, y=160)
                    self.brt = Button(self, text='FIND',bg='black', fg='white', width=15, font=('times roman', 12),command = ent).place(x=1000, y=150)
                    
                    self.label7 = Label(self, text="INFORMATION DETAILS",bg='brown', fg='white',  font=('times roman', 15, 'underline', 'bold'))
                    self.label7.place(x=560, y=300)
                    self.button = Button(self, text='SEARCH READER', width=25 ,bg='black', fg='white',font=('times roman', 10), command=sest).place(x=225,y=250) #doing
                    self.button = Button(self, text='SEARCH BOOK', width=25,bg='black', fg='white', font=('times roman', 10), command=sea).place(x=485,y=250)#doing
                    self.brt = Button(self, text="ISSUE BOOK", width=25,bg='black', fg='white' ,font=('times roman', 10), command=ib).place(x=735, y=250)#doing
                    self.brt = Button(self, text="RETURN BOOK", width=25,bg='black', fg='white' ,font=('times roman', 10), command=ret).place(x=985, y=250)#doing
                    self.brt = Button(self, text="LOGOUT", width=15,bg="red", font=('times roman', 10), command=log).place(x=1150, y=105)
            except Error:
                messagebox.showerror("ERROR", "Something Went Wrong!")
        check()

MainWin().mainloop()
