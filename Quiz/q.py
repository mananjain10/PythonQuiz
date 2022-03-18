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
conn=sqlite3.connect('koko.db')

print("connection is successful")

conn.execute('CREATE TABLE IF NOT EXISTS game (username TEXT NOT NULL, tscore INT NOT NULL, score INT NOT NULL );')
c=conn.execute('SELECT * FROM game WHERE username=?',(content,));
if c.fetchall():
    print('hiiii')
else:
    c.execute('INSERT INTO game VALUES (?,?,?)',(content,10,0));
    conn.commit()

class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = Label(view, text="Right!", font="TimesNewRoman 12 bold", fg="green",bg="black")
            right += 1
        else:
            label = Label(view, text="Wrong!", font="TimesNewRoman 12 bold", fg="red",bg="black")
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))

    def getView(self, root):
        view = Frame(root, bg="black")
        Label(view, text=self.question, font="TimesNewRoman 16 bold", fg="pink",bg="black").pack()
        Button(view, text=self.answers[0], command=lambda *args: self.check("A", view)).pack()
        Button(view, text=self.answers[1], command=lambda *args: self.check("B", view)).pack()
        Button(view, text=self.answers[2], command=lambda *args: self.check("C", view)).pack()
        Button(view, text=self.answers[3], command=lambda *args: self.check("D", view)).pack()
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

def askQuestion():
    def certo():
        os.system('certi.py')
    file=open("uss.txt","r")
    content=file.read()
    file.close()
    global questions, root, index, button, right, number_of_questions
    if(len(questions) == index + 1):
        Label(root, text= "Hello " + content, font="TimesNewRoman 16 bold", fg="orange",bg="black").pack(pady=10)
        Label(root, text= "Current Score: " +str(right), font="TimesNewRoman 16 bold", fg="orange",bg="black").pack(pady=10)
        b=Button(root,text='certificate',command=certo,font="TimesNewRoman 20 bold")
        b.pack(side=BOTTOM)
        hs=right
        conn=sqlite3.connect('koko.db')
        print("connection is successful")
        c=conn.execute('SELECT score FROM game WHERE ? > score',(right,))
        if c.fetchall():
              c.execute('UPDATE game SET score=? WHERE username=?',(right,content,))
              #print(right)
              Label(root, text= "High Score: " +str(right), font="TimesNewRoman 16 bold", fg="orange",bg="black").pack(pady=10)
              conn.commit()
              #conn.close()
        else:
            print('No high score') #table waala score
            c=conn.execute("SELECT username, tscore, score from game where username=?", (content,))
            for i in c:
                #print("Score: ", i[2])
                Label(root, text= "High Score: " +str(i[2]), font="TimesNewRoman 16 bold", fg="orange",bg="black").pack(pady=10)
        conn.close()


        return
    button.pack_forget()
    index += 1
    questions[index].getView(root).pack()


questions = []
file = open("questions.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range (4):
        answers.append(file.readline())

    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)

root = Tk()
root.title('Quiz')
root.configure(bg="black")
root.geometry("500x300")
def a():
  load = Image.open("quiz.png")
  load = load.resize((200, 100), Image.ANTIALIAS)
  render = ImageTk.PhotoImage(load)
  # labels can be text or images
  img = Label(root, image=render)
  img.image = render
  img.place(x=0,y=0)


'''button=Button(root)
photo=PhotoImage(file="quiz.png")
button.config(image=photo,width="400",height="200",activebackground="black",bg="black",command=askQuestion)
button.place(x=50, y=5, anchor=NW)'''



photo=PhotoImage(file="quiz.png")
button = Button(root,image=photo,width="450",height="250", command=askQuestion, font="TimesNewRoman 20 bold")
button.pack()
root.mainloop()
