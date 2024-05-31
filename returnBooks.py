from tkinter import *
from tkinter import messagebox
import mysql.connector


def return_db():
    global id

    book_id = id.get()

    db = mysql.connector.connect(host="localhost", user="root", password='pythonproject', database='db')
    cursor = db.cursor()

    print(book_id, end='--')
    print("return")

    try:
        checkavailability = " select * from books where availability='NO';"
        print(checkavailability)
        cursor.execute(checkavailability)

        flag = 0

        for i in cursor:
            print(i[0])
            if (i[0] == book_id):
                flag = 1
                break;

        if flag == 1:
            updatequery = "update books set availability='YES' where book_id='" + book_id + "';"
            print(updatequery)
            cursor.execute(updatequery)
            db.commit()

            sqlquery = "delete from issue where book_id='" + book_id + "';"
            print(sqlquery)

            cursor.execute(sqlquery)
            db.commit()

            messagebox.showinfo('Success', "Book returned Successfully")
        else:
            messagebox.showinfo("Error", "Invalid Book id")
    except:
        messagebox.showinfo("Error", "Cannot return given book ")


def returnBooks():
    global id

    window = Tk()
    window.geometry("600x170")
    window.title('DoubleJKP Library Management System')
    window.configure(background='#1b4d33')

    greet = Label(window, font=('Times New Roman', 33, 'bold'), text="Return Books", bg='#1b4d33',fg='gold')
    greet.grid(row=0, columnspan=3, padx=5, pady=5)

    L = Label(window, font=('Times New Roman', 18), text="Enter Book ID :",bg='#1b4d33',fg='gold')
    L.grid(row=2, column=0, padx=2, pady=2)

    id = Entry(window, width=25, font=('Times New Roman', 18))
    id.grid(row=2, column=3, padx=5, pady=5)

    submitbtn = Button(window, text="Submit", width=12, command=return_db, bg='#1b4d33',fg='gold', font=('arial', 15, 'bold'))
    submitbtn.grid(row=8, column=2, columnspan=3, padx=5, pady=5)

    print("return")
    pass