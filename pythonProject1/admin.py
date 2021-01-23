from tkinter import *
import mysql.connector
from tkinter import messagebox as mb
import tkinter as tk
from datetime import *

import admin_backend as backend
window = Tk()
window.resizable(False,False)
window.geometry("600x600")


def display_data():
    mydb = mysql.connector.connect(user="lifechoices",
    password="@Lifechoices1234",
    host="localhost",
    database="lifechoicesonline",
    auth_plugin="mysql_native_password")


    mycursor = mydb.cursor()
    try:
        x = mycursor.execute("select * from users")

        
        for i in mycursor:
            list_box.insert('end',i)

    except:
        mb.showerror("Error","Error in sql")

def delete():
    fn = fullname.get()
    con = mysql.connector.connect(host="localhost", database="lifechoicesonline", user="lifechoices", password="@Lifechoices1234")
    cur = con.cursor()
    cur.execute("DELETE FROM users WHERE full_name=%s",[(fn)])
    con.commit()

    mb.showinfo("Information","Record Deleted")           

def add_user():
    mydb = mysql.connector.connect(user="lifechoices",
    password="@Lifechoices1234",
    host="localhost",
    database="lifechoicesonline",
    auth_plugin="mysql_native_password")

    fn = fullname.get()
    un = username.get()
    pw = password.get()
    mn = mobilenumber.get()
    cursor = mydb.cursor()
    sql="insert into users(full_name,user_name,password,mobile_number) values(%s,%s,%s,%s)"
    try:
        cursor.execute(sql,[(fn),(un),(pw),(mn)])
        mydb.commit()
        mb.showinfo("Success","Added user "+un+" successfully")
    except:
        mb.showerror("Error","Error in sql")




lbluser=tk.Label(window, text="Administration", bg="white")
lbluser.pack(pady=10)

list_box = Listbox(window,bg="white",width=50,selectbackground="grey", selectforeground="black")
list_box.pack(pady=20, padx=10)
list_box.bind(display_data)

lbl1 = Label(window, text="Full Name: ")
lbl1.pack()
fullname = Entry(window)
fullname.pack()
lbl2 = Label(window, text="User Name: ")
lbl2.pack()
username = Entry(window)
username.pack()
lbl3 = Label(window, text="Password: ")
lbl3.pack()
password = Entry(window)
password.pack()
lbl4 = Label(window, text="Mobile Number: ")
lbl4.pack()
mobilenumber = Entry(window)
mobilenumber.pack()
lblinstruct = Label(window, text="Press 'Display Data' to show information within the database.")
lblinstruct.place(x=10, y=450)
lbladduser = Label(window, text="Enter user information then click 'ADD' to store user info in database and create account.")
lbladduser.place(x=10, y=470)
lblinstruct1 = Label(window, text="Enter name of user in 'Full Name' then click 'DELETE' to remove user from database.")
lblinstruct1.place(x=10, y=490)
lblinstruct2 = Label(window, text="In order to refresh database, click 'CLEAR' then 'Display Data'.")
lblinstruct2.place(x=10, y=510)


display = Button(window, text="Display Data", command=display_data)
display.place(x=20, y=565)
adduser = Button(window, text="ADD", command=add_user)
adduser.place(x=160, y=565)
delete = Button(window, text="DELETE", command=delete)
delete.place(x=240, y=565)
grantpriv = Button(window, text="Grant Privileges")
grantpriv.place(x=450, y=565)

def clearlist():
    list_box.delete(0,END)


clearbtn = Button(window, text="CLEAR", command=clearlist)
clearbtn.place(x=515, y=150)

window.mainloop()

