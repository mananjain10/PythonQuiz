from tkinter import *
from tkinter import messagebox as ms
from time import sleep
import l
import sqlite3
import sys
import os
from PIL import ImageTk,Image

file=open("uss.txt","r")
content=file.read()
file.close()
print(content)
root=Tk()
root.title('Certificate')
root.configure(bg="white")
'''canvas = Canvas(root, width = 1000, height = 900)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("rait.png"))
canvas.create_image(0, 0, anchor=NW,image=img)'''
load = Image.open("rait.png")
load = load.resize((160, 85), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
# labels can be text or images
img = Label(root, image=render)
img.image = render
img.place(x=10, y=10)
Label(root, text='Certificate' ,font="TimesNewRoman 45 bold", fg="red",bg="white").pack(pady=90)
Label(root, text='This is to certify that ' + content+' of computer ',font="TimesNewRoman 16 bold", fg="black",bg="white").pack(pady=0)
conn=sqlite3.connect('koko.db')
c=conn.execute("SELECT username, tscore, score from game where username=?", (content,))
for i in c:
    #print("Score: ", i[2])
    #Label(root, text= "High Score: " +str(i[2]), font="TimesNewRoman 16 bold", fg="orange",bg="black").pack(pady=10)
    Label(root, text='engineering department has scored ' + str(i[2])+' in the ',font="TimesNewRoman 16 bold", fg="black",bg="white").pack(pady=0)

conn.close()
Label(root, text='quiz on python organized by ',font="TimesNewRoman 16 bold", fg="black",bg="white").pack(pady=0)
Label(root, text='Manan Bohra',font="TimesNewRoman 16 bold", fg="black",bg="white").pack(pady=0)





root.geometry('600x400')
root.mainloop()
