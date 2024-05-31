from tkinter import *
from tkinter import messagebox
import mysql.connector


def delete_db():
    global id

    book_id = id.get()

    db = mysql.connector.connect(host="localhost", user="root", password='pythonproject', database='db')
    cursor = db.cursor()

    print(book_id, end='--')
    print("delete")

    sqlquery = "delete from books where book_id='" + book_id + "';"
    print(sqlquery)

    try:
        cursor.execute(sqlquery)
        db.commit()
        messagebox.showinfo('Success', "Book deleted Successfully")
    except:
        messagebox.showinfo("Error", "Book with given id does not exist")


def deleteBooks():
    global id

    window = Tk()
    window.geometry("600x170")
    window.title('DoubleJKP Library Management System')
    window.configure(background='#1b4d33')

    greet = Label(window, font=('Times New Roman', 33, 'bold'), text="Delete Books", bg='#1b4d33',fg='gold')
    greet.grid(row=0, columnspan=2, padx=5, pady=5)

    # ----------id-------------------

    L = Label(window, font=('Times New Roman', 18), text="Enter Book ID :",bg='#1b4d33',fg='gold')
    L.grid(row=2, column=0, padx=2, pady=2)

    id = Entry(window, width=25, font=('Times New Roman', 18))
    id.grid(row=2, column=3, padx=2, pady=5)

    submitbtn = Button(window, text="Submit", width=12, command=delete_db, bg='#1b4d33',fg='gold',font=('Times New Roman', 18, 'bold'))
    submitbtn.grid(row=8, column=2, columnspan=3, padx=5, pady=5)

    print("delete")
    pass