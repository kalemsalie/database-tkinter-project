from tkinter import *
import mysql.connector
from tkinter import messagebox as mb
import tkinter as tk
from datetime import *


mydb = mysql.connector.connect(user="lifechoices",
password="@Lifechoices1234",
host="localhost",
database="lifechoicesonline",
auth_plugin="mysql_native_password")

cursor = mydb.cursor()

window = Tk()
window.resizable(False,False)
window.geometry("600x200")
lbl1 = Label(window,text="Username: ")
user_entry = Entry(window)
lbl2 = Label(window,text="Password: ")
password_entry = Entry(window)
lbl3 = Label(window,text="For Admin Page hold Ctrl & A")

def reg():
    window2 = Tk()
    window.resizable(False,False)
    lb = Label(window2, text="Full Name: ")
    name_entry = Entry(window2)
    lbl1 = Label(window2,text="Username: ")
    user_entry = Entry(window2)
    lbl2 = Label(window2,text="Password: ")
    password_entry = Entry(window2)
    lbl3 = Label(window2,text="Phone Number: ")
    phone_entry = Entry(window2)

    def insertreg():
        username = (name_entry.get(),user_entry.get(),password_entry.get(), phone_entry.get())
        cmd = "INSERT INTO users (full_name, user_name, password, mobile_number) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(cmd, username)
            mydb.commit()
            mb.showinfo("Success","didit")
            window2.destroy()
        except:
            mb.showerror('error','sql error')
    btn = Button(window2, text="Register", command=insertreg)
    lb.pack()
    name_entry.pack()
    lbl1.pack()
    user_entry.pack()
    lbl2.pack()
    password_entry.pack()
    lbl3.pack()
    phone_entry.pack()
    btn.pack()
    window2.mainloop()
btn2 = Button(window, text="Register New User", command=reg)

def login():
    try:
        usern = user_entry.get()
        pswrd = password_entry.get()
        signin = "select * from users where user_name=%s and password=%s"
        cursor.execute(signin,[usern,pswrd])
        fetch = cursor.fetchall()
        time = datetime.now()
        clock = time.strftime("%H:%M:%S")
        day = time.strftime("%d/%m/%y")
        


        
        if fetch:
            for i in fetch:
                mb.showinfo("Message", "Welcome")
                window.destroy()
                window3 = Tk()
                def out():
                    d = datetime.now()
                    logout = d.strftime("%H:%M:%S")
                    cmd = "INSERT INTO time(username, date, logintime, logouttime) VALUES (%s, %s, %s, %s)"

                    cursor.execute(cmd, [(usern), (day), (clock), (logout)])
                    mydb.commit()
                btn4 = Button(window3, text="Logout", command=out)
                btn4.pack()
                window3.mainloop()


                break

        else:
            failed()                                 

            
    except:
        mb.showerror("Login Failed","Please Check Username and Password, If You Do Not Have An Account Please Register")       
btn3 = Button(window, text="login", command=login)

lbl1.pack()
user_entry.pack()
lbl2.pack()
password_entry.pack()
btn2.pack()
btn3.pack()
lbl3.pack()

keyspressed = ""
def key():
    global keyspressed
    window.destroy()
    import admin

window.bind("<Control-a>", lambda x: key())



    

window.mainloop()
