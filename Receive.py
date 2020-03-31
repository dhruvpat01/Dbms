import sqlite3
from tkinter import *
from Fullscrn import *
from tkinter import messagebox
import re

def receive(a,email):
    t = Tk()

    pname2 = StringVar()
    page2 = IntVar()
    pblood=StringVar()
    pamount2=IntVar()
    a.destroy()
    t.title("Blood Bank")
    t.geometry("500x500+120+120")
    t.configure(background="grey")
    Frame1 = Frame(t)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    # name1 = Label(Frame1)
    # name1.place(relx=0.25, rely=0.05, height=33, width=200)
    # name1.configure(background="#d9d9d9", text="Enter name", font=("Times", 10), width=1000)
    # name2 = Entry(t)
    # name2.get()
    # name2.place(relx=0.42, rely=0.07, height=33, width=200)

    # email1 = Label(Frame1)
    # email1.place(relx=0.25, rely=0.05, height=33, width=200)
    # email1.configure(background="#d9d9d9", text="Enter Username", font=("Times", 10), width=200)
    # email2 = Entry(t)
    # email2.place(relx=0.42, rely=0.07, height=33, width=500)


    pname1 = Label(Frame1)
    pname1.place(relx=0.25, rely=0.15, height=33, width=200)
    pname1.configure(background="#d9d9d9", text="Enter Patient  name", font=("Times", 10), width=200)
    pname2 = Entry(t)
    pname2.place(relx=0.42, rely=0.17, height=33, width=500)

    psex = Label(Frame1)
    psex.place(relx=0.25, rely=0.25, height=33, width=200)
    psex.configure(background="#d9d9d9", text="Select Sex of Patient ", font=("Times", 10))
    sex = StringVar(t, value="0")
    radiobutton1 = Radiobutton(Frame1, text="Male", variable=sex, value="Male",font=("Times", 10))
    radiobutton1.place(relx=0.45, rely=0.27)
    radiobutton2 = Radiobutton(Frame1, text="Female", variable=sex, value="Female",font=("Times", 10))
    radiobutton2.place(relx=0.55, rely=0.27)
    radiobutton3 = Radiobutton(Frame1, text="Other", variable=sex, value="Other",font=("Times", 10))
    radiobutton3.place(relx=0.65, rely=0.27)

    page1 = Label(Frame1)
    page1.place(relx=0.25, rely=0.37, height=33, width=200)
    page1.configure(background="#d9d9d9", text="Enter Age", font=("Times", 10))
    page2 = Entry(t)
    page2.get()
    page2.place(relx=0.42, rely=0.37, height=33, width=200)

    blood = StringVar(Frame1)
    pblood = Label(t, text="Select Blood Group Required")
    pblood.configure(background="#d9d9d9",font=("Times", 10))
    pblood.place(relx=0.26, rely=0.47,height=33,width=200)
    values = ["A Positive",
              'A Negative',
              'B Positive',
              'B Negative',
              'AB Positive',
              'AB Negative',
              'O Positive',
              'O Negative']
    blood.set('Select Blood Type')
    dropdown = OptionMenu(t, blood, *values)
    dropdown.place(relx=0.42, rely=0.47,height=33,width=200)


    pamount1 = Label(Frame1)
    pamount1.place(relx=0.25, rely=0.65, height=33, width=200)
    pamount1.configure(background="#d9d9d9", text="Enter Amount of blood required in bags", font=("Times", 8))
    pamount2 = Entry(t)

    pamount2.place(relx=0.42, rely=0.63, height=33, width=200)

    # number1 = Label(Frame1)
    # number1.place(relx=0.25, rely=0.75, height=33, width=200)
    # number1.configure(background="#d9d9d9", text="Enter Phone Number", font=("Times", 10))
    # number2 = Entry(t)
    # number2.get()
    # number2.place(relx=0.42, rely=0.72, height=33, width=200)


    Button_Submit = Button(Frame1, text="Submit", padx=30, pady=10, font=("Times", 20),command=lambda: display1(pname2.get(),page2.get(),sex.get(),blood.get(),pamount2.get(),email,t))
    Button_Submit.place(relx=0.35, rely=0.82, height=45, width=300,)
    full4=FullScreenApp(t)
    t.mainloop()

conn = sqlite3.connect("Blood_Bank.db")
co = conn.cursor()

def add(name,age,sex,blood,amount,email):
    co.execute("UPDATE Blood_Inventory SET No_of_Bags=No_of_Bags-1 where Blood_Group=(?)",(blood,))
    co.execute("INSERT INTO Receiver VALUES(?,?,?,?,?,?)", (email,name,sex,age,blood,amount ))
    conn.commit()

def display1(name, age,sex,blood,amount,email,t):
    if not (re.search("[A-Za-z_ ]", name)):
        r = messagebox.showerror("popup", "Name should only contain character")

    elif not (re.search("\d", age)):
        q = messagebox.showerror("popup", "only integer is valid")
    elif not (re.search("[\d]{1,3}", amount)):
        we = messagebox.showerror("popup", "please enter correct amount")

    elif not (re.search("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", email)):
        d = messagebox.showwarning("popup", "email is invalid")

    else:

        add(name, age, sex, blood, amount, email)
        dumb = Tk()

        # t.destroy()
        # label1 = Label(dumb, text=e)
        # label1.pack()

        label2 = Label(dumb, text="Blood Received Successfully")
        label2.pack()
        full9 = FullScreenApp(dumb)
        dumb.mainloop()
