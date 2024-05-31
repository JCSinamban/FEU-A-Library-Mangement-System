from tkinter import *
import mysql.connector

from add import *
from delete import *
from issue import *
from returnBooks import *
from view import *
from viewissue import *

db = mysql.connector.connect(host="localhost", user="root", password='pythonproject', database='db')
cursor = db.cursor()

window = Tk()
window.geometry("1200x650")
window.title("DoubleJKP Library Management System")

pic = PhotoImage(file="pythonbg.png")

my_label = Label(window, image=pic)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

greet = Label(window, font=('Times New Roman', 33, 'bold'), text="Welcome to FEU-A Library Management System", bg='#1b4d33', fg="Gold")
greet.grid(row=0, column=4, columnspan=5, padx=140, pady=40)

addbtn = Button(window, text="Add Books", width=18, height=1,command=addBooks, bg="Gold", fg="Darkgreen", font=('Times New Roman', 23, 'bold'))
addbtn.grid(row=3, column=4, columnspan=5, padx=5, pady=10)

deletebtn = Button(window, text="Delete Books",width=18, height=1, command=deleteBooks, bg="Gold", fg="Darkgreen", font=('Times New Roman', 23, 'bold'))
deletebtn.grid(row=5, column=4,  columnspan=5, padx=5, pady=10)

issuebtn = Button(window, text="Issue Books", width=18, height=1, command=issueBooks, bg="Gold", fg="Darkgreen",font=('Times New Roman', 23, 'bold'))
issuebtn.grid(row=7, column=4, columnspan=5, padx=5, pady=10)

returnbtn = Button(window, text="Return Books", width=18, height=1, command=returnBooks, bg="Gold", fg="Darkgreen",font=('Times New Roman', 23, 'bold'))
returnbtn.grid(row=9, column=4, columnspan=5, padx=5, pady=10)

viewbtn = Button(window, text="View Books", width=18, height=1, command=viewBooks, bg="Gold", fg="Darkgreen", font=('Times New Roman', 23, 'bold'))
viewbtn.grid(row=11, column=4, columnspan=5, padx=5, pady=10)

viewissuebtn =Button(window, text="View Issued Books", width=18, height=1, command=issuedBooks, bg="Gold", fg="Darkgreen", font=('Times New Roman', 23, 'bold'))
viewissuebtn.grid(row=13, column=4, columnspan=6, padx=5, pady=10)


window.mainloop()