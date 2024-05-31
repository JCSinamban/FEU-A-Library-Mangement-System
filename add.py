from tkinter import *
from tkinter import messagebox
import mysql.connector


def add_db():
    global id
    global title
    global author

    book_id = id.get()
    book_title = title.get()
    book_author = author.get()

    db = mysql.connector.connect(host="localhost", user="root", password='pythonproject', database='db')
    cursor = db.cursor()

    print(book_id, end='--')
    print(book_title, end='--')
    print(book_author, end='--')
    print("add")

    sqlquery = "insert into books values('" + book_id + "','" + book_title + "','" + book_author + "','YES');"
    print(sqlquery)

    try:
        cursor.execute(sqlquery)
        db.commit()
        messagebox.showinfo('Success', "Book added Successfully")
    except:
        messagebox.showinfo("Error", "Cannot add given book data into Database")


def addBooks():
    global id
    global title
    global author

    window = Tk()
    window.geometry("600x250")
    window.title('DoubleJKP Library Management System')
    window.configure(background='#1b4d33')

    greet = Label(window, font=('Times New Roman', 33, 'bold'), text="Add Books", bg='#1b4d33',fg='gold')
    greet.grid(row=0, columnspan=3)

    # ----------id-------------------

    L = Label(window, font=('Times New Roman', 18), text="Enter Book ID :", bg='#1b4d33',fg='gold')
    L.grid(row=4, column=1, padx=5, pady=5)

    id = Entry(window, width=30, font=('Times New Roman', 18))
    id.grid(row=4, column=3, padx=5, pady=5)

    # ----------title-------------------

    L = Label(window, font=('Times New Roman', 18), text="Enter Title :      ", bg='#1b4d33',fg='gold')
    L.grid(row=7, column=1, padx=5, pady=5)

    title = Entry(window, width=30, font=('Times New Roman', 18))
    title.grid(row=7, column=3, padx=5, pady=5)

    # ----------author-------------------

    L = Label(window, font=('Times New Roman', 18), text="Enter Author :  ", bg='#1b4d33',fg='gold')
    L.grid(row=9, column=1, padx=5, pady=5)

    author = Entry(window, width=30, font=('Times New Roman', 18))
    author.grid(row=9, column=3, padx=5, pady=5)

    submitbtn = Button(window, text="Submit", width=12, command=add_db, bg="#1b4d33", fg="gold",
                       font=('Times New Roman', 18, 'bold'))
    submitbtn.grid(row=12, column=3, columnspan=3, padx=5, pady=5)

    print("add")
    pass