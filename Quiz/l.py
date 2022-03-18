from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import sys
import os

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('qaz.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT PRIMARY KEY ,password TEXT NOT NULL);')
db.commit()
db.close()

#main Class
class main:
    def __init__(self,master):
    	# Window
        self.master = master

        # Some Useful variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()

    def users(self):
           self.head['text'] = self.username.get() + '\n Loged In'

    #Login Function
    def login(self):

        file=open("uss.txt","w")
        content=file.write(str(self.username.get()))
        file.close()

    	#Establish Connection
        with sqlite3.connect('qaz.db') as db:
            c = db.cursor()
        #q.py
        def yoyo():
            os.system('q.py')
        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            yoyo()
        else:
            ms.showerror('Oops!','Username Not Found.')

    def new_user(self):
    	#Establish Connection
        with sqlite3.connect('qaz.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.username.get())])
        if c.fetchall():
            ms.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Create New Account
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()

        #Frame Packing Methords
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    #Draw Widgets
    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',pady = 10, font="TimesNewRoman 40 bold", fg="cyan", bg="black")
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10, bg="black")
        Label(self.logf,text = 'Username: ',pady=5,padx=5, font="TimesNewRoman 18 bold", fg="pink",bg="black").grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',pady=20,padx=5, font="TimesNewRoman 18 bold", fg="pink",bg="black").grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Sign in ',bd = 3 ,padx=10,pady=10,command=self.login, font="TimesNewRoman 12 bold", fg="black", bg="grey").grid()
        Button(self.logf,text = ' Sign up ',bd = 3 ,padx=10,pady=10,command=self.cr, font="TimesNewRoman 12 bold", fg="black", bg="grey").grid(row=2,column=1)
        self.logf.pack()

        self.crf = Frame(self.master,padx =10,pady = 10, bg="black")
        Label(self.crf,text = 'Username: ',pady=5,padx=5, font="TimesNewRoman 18 bold", fg="pink",bg="black").grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',pady=20,padx=5, font="TimesNewRoman 18 bold", fg="pink",bg="black").grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.crf,text = 'Create account',bd = 3 ,padx=5,pady=5,command=self.new_user,font="TimesNewRoman 12 bold", fg="black", bg="grey").grid()
        Button(self.crf,text = 'Go to Login',bd = 3 ,padx=5,pady=5,command=self.log,font="TimesNewRoman 12 bold",fg="black", bg="grey").grid(row=2,column=1)

if __name__ == '__main__':
	#Create Object
	#and setup window
    root = Tk()
    root.title('Login Form')
    root.configure(bg="black")
    print("yoyo")
    #root.geometry('400x350+300+300')
    main(root)

    root.mainloop()
