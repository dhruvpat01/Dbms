import sqlite3
from tkinter import *
from sqlite3 import *
from Fullscrn import *


def user11(a):
    a.destroy()
    b = Tk()
    b.title("Update User")

    Frame1 = Frame(b)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    email1 = Label(Frame1)
    email1.place(relx=0.30, rely=0.45, height=33, width=200)
    email1.configure(background="#d9d9d9", text="Enter Email:", font=("Times", 10), width=1000)
    email2 = Entry(b)
    email2.place(relx=0.47, rely=0.45, height=33, width=200)

    update1 = Button(Frame1, background="#d9d9d9", text="Update", fg='black', font=("Times", 25), width=200,
                     command=lambda: user22(b, email2.get()))
    update1.place(relx=0.47, rely=0.57, height=43, width=200)
    update1.configure()

    full11 = FullScreenApp(b)
    b.mainloop()

conn = sqlite3.connect("Blood_Bank.db")
co = conn.cursor()

def user22(a, email):
    co.execute("SELECT Name,Sex,Age,PhoneNumber,Password FROM User WHERE Email=(?)", (email,))
    details = co.fetchone()

    a.destroy()
    c = Tk()
    c.title("Update User Info")

    Frame1 = Frame(c)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    det = Label(Frame1, text=details, font=("Times", 10), width=1000)
    det.place(relx=0.27, rely=0.05, height=33, width=600)

    name1 = Label(Frame1)
    name1.place(relx=0.30, rely=0.13, height=33, width=200)
    name1.configure(background="#d9d9d9", text="Enter name", font=("Times", 10), width=1000)
    name2 = Entry(c)
    name2.place(relx=0.47, rely=0.15, height=33, width=200)

    sex = Label(Frame1)
    sex.place(relx=0.30, rely=0.25, height=33, width=200)
    sex.configure(background="#d9d9d9", text="Select Sex ", font=("Times", 10))
    v = StringVar(Frame1, value="b")
    radiobutton1 = Radiobutton(Frame1, text="Male", variable=v, value="Male", font=("Times", 10))
    radiobutton1.place(relx=0.50, rely=0.25)
    radiobutton2 = Radiobutton(Frame1, text="Female", variable=v, value="Female", font=("Times", 10))
    radiobutton2.place(relx=0.60, rely=0.25)
    radiobutton3 = Radiobutton(Frame1, text="Other", variable=v, value="Other", font=("Times", 10))
    radiobutton3.place(relx=0.70, rely=0.25)

    age1 = Label(Frame1)
    age1.place(relx=0.30, rely=0.35, height=33, width=200)
    age1.configure(background="#d9d9d9", text="Enter Age", font=("Times", 10), width=1000)
    age2 = Entry(c)
    age2.place(relx=0.47, rely=0.35, height=33, width=200)

    pno1 = Label(Frame1)
    pno1.place(relx=0.30, rely=0.45, height=33, width=200)
    pno1.configure(background="#d9d9d9", text="Enter Phone Number", font=("Times", 10), width=1000)
    pno2 = Entry(c)
    pno2.place(relx=0.47, rely=0.45, height=33, width=200)

    password1 = Label(Frame1)
    password1.place(relx=0.30, rely=0.55, height=33, width=200)
    password1.configure(background="#d9d9d9", text="Enter Password", font=("Times", 10), width=1000)
    password2 = Entry(c)
    password2.place(relx=0.47, rely=0.55, height=33, width=200)

    update11 = Button(Frame1, background="#d9d9d9", text="Update", fg='black', font=("Times", 25), width=200,
                     command=lambda: display1(name2.get(), v.get(), age2.get(), pno2.get(), password2.get(),email,c))
    update11.place(relx=0.47, rely=0.67, height=43, width=200)

    full11 = FullScreenApp(c)
    c.mainloop()


def update1(name, sex, age, pno, password,email):
    co.execute("UPDATE User SET Name=(?),sex=(?),Age=(?),PhoneNumber=(?),Password=(?) WHERE Email=(?)",
               (str(name), str(sex), int(age), int(pno), str(password), str(email),))
    conn.commit()

def display1(name,sex,age,pno,password,email,a):
    update1(name,sex,age,pno,password,email)
    a.destroy()
    d=Tk()

    Frame1 = Frame(d)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    data1 = Label(Frame1)
    data1.place(relx=0.30, rely=0.45, height=33, width=500)
    data1.configure(background="#d9d9d9", text="Data Updated:", font=("Times", 10), width=1000)

    full11 = FullScreenApp(d)
    d.mainloop()