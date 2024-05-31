from tkinter import *
from tkinter import messagebox
import mysql.connector


def issue_db():
    global id
    global StudentName

    book_id = id.get()
    student_name = StudentName.get()

    db = mysql.connector.connect(host="localhost", user="root", password='pythonproject', database='db')
    cursor = db.cursor()

    print(book_id, end='--')
    print(student_name, end='--')
    print("issue")

    try:
        checkavailability = " select * from books where availability='YES';"
        print(checkavailability)
        cursor.execute(checkavailability)

        flag = 0

        for i in cursor:
            print(i[0])
            if (i[0] == book_id):
                flag = 1


        if flag == 1:
            updatedb = "update books set availability='NO' where book_id='" + book_id + "';"
            print(updatedb)
            cursor.execute(updatedb)
            db.commit()

            query = "insert into issue (book_id, student_name) values('"+ book_id +"', '" + student_name + "')"
            print(query)
            cursor.execute(query)
            db.commit()

            messagebox.showinfo('Success', "Book issued Successfully")
        else:
            messagebox.showinfo("Error", "Required Book is not available")
    except:
        messagebox.showinfo("Error", "Cannot issue given book ")



def issueBooks():
    global id
    global StudentName

    window = Tk()
    window.geometry("600x220")
    window.title('DoubleJKP Library Management System')
    window.configure(background='#1b4d33')

    greet = Label(window, font=('Times New Roman', 33, 'bold'), text="Issue Books",bg='#1b4d33',fg='gold')
    greet.grid(row=0, columnspan=3, padx=5, pady=5)

    # ----------id-------------------

    L = Label(window, font=('Times New Roman', 18), text="Enter Book ID:          ", bg='#1b4d33',fg='gold')
    L.grid(row=2, column=1, padx=5, pady=5)

    id = Entry(window, width=27, font=('Times New Roman', 18))
    id.grid(row=2, column=3, padx=5, pady=5)

    # ----------StudentName-------------------

    L = Label(window, font=('Times New Roman', 18), text="Enter Student Name: ", bg='#1b4d33',fg='gold')
    L.grid(row=4, column=1, padx=2, pady=2)

    StudentName = Entry(window, width=27, font=('Times New Roman', 18))
    StudentName.grid(row=4, column=3, padx=5, pady=5)

    submitbtn = Button(window, text="Submit", width=12, command=issue_db, bg='#1b4d33',fg='gold',font=('Times New Roman', 18, 'bold'))
    submitbtn.grid(row=8,column=3,columnspan=6, padx=5, pady=5)

    print("issue")

    pass