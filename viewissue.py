from tkinter import *
from tkinter import messagebox
import mysql.connector


def issuedBooks():
    global id

    window = Tk()
    window.geometry("550x400")
    window.title('DoubleJKP Library Management System')
    window.configure(background='#1b4d33')

    greet = Label(window, font=('Times New Roman', 33, 'bold'), text="View List of Issued Books", bg='#1b4d33',fg='gold')
    greet.grid(row=0, columnspan=7, padx=2, pady=2)

    db = mysql.connector.connect(host="localhost", user="root", password='pythonproject', database='db')
    cursor = db.cursor()

    sqlquery = "select * from issue ;"
    print(sqlquery)

    try:
        cursor.execute(sqlquery)
        # db.commit()
        L = Label(window, font=('Times New Roman', 23), text="%-10s%-20s" % ('       Book ID         ', 'Student Name'),bg='#1b4d33',fg='gold')
        L.grid(row=2,  column=1, columnspan=4, padx=2, pady=2)

        L = Label(window, font=('Times New Roman', 23), text="       --------------------------------------------", bg='#1b4d33',fg='gold')
        L.grid(row=3, column=1, columnspan=4, padx=2, pady=2)

        x = 4
        for i in cursor:
            L = Label(window, font=('Times New Roman', 18), text="%-10s%-10s" % (i[0],i[1]), bg='#1b4d33',fg='gold')
            L.grid(row=x, column=1, columnspan=4, padx=2, pady=2)
            x += 1

    except:
        messagebox.showinfo("Error", "Cannot Fetch data.")

    print("view")
    pass