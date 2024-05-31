from tkinter import *
from tkinter import messagebox
import mysql.connector


def viewBooks():
    global id

    window = Tk()
    window.geometry("1090x550")
    window.title('DoubleJKP Library Management System')
    window.configure(background='#1b4d33')

    greet = Label(window, font=('Times New Roman', 33, 'bold'), text="View List of Books", bg='#1b4d33',fg='gold')
    greet.grid(row=0, columnspan=2)

    db = mysql.connector.connect(host="localhost", user="root", password='pythonproject', database='db')
    cursor = db.cursor()

    sqlquery = "select * from books ;"
    print(sqlquery)
    try:
        cursor.execute(sqlquery)
        # db.commit()
        L = Label(window, font=('Times New Roman', 23), text="%-20s%-30s%-20s%-20s" % ('Book ID', 'Title', 'Author', 'Availability'),bg='#1b4d33',fg='gold')
        L.grid(row=1, columnspan=4, padx=150)

        L = Label(window, font=('Times New Roman', 23), text="  ----------------------------------------------------------------------------------------------------", bg='#1b4d33',fg='gold')
        L.grid(row=2, columnspan=1)

        x = 4
        for i in cursor:
            L = Label(window, font=('Times New Roman', 18), text="%-20s%-40s%-35s%-0s" % (i[0], i[1], i[2], i[3]),bg='#1b4d33',fg='gold')
            L.grid(row=x, columnspan=1)
            x += 1

    except:
        messagebox.showinfo("Error", "Cannot Fetch data.")

    print("view")
    pass