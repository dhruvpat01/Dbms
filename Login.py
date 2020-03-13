from tkinter import *
from tkinter import messagebox
from Main import *
from Receive import*
from nextpage import *
import re


def loginbut(a, b, c, d):
    if not (re.search("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", a)):
        d = messagebox.showwarning("popup", "email is invalid")

    elif not (re.search("[\w@$&_!]{8,14}", b)):
        e = messagebox.showwarning("popup", "password is weak or too short")


    elif not (c == b):
        a = messagebox.showwarning("popup", "your passwords do not match")
    else:
        root1 = Tk()
        root1.title("Blood Bank")
        root1.geometry("400x400")
        root1.configure(background="grey")
        Frame1 = Frame(root1)
        Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
        Frame1.configure(borderwidth="2", background="grey", width=500)

        Button3 = Button(Frame1)
        Button3.place(relx=0.35, rely=0.69, height=53, width=100)
        Button3.configure(background="#d9d9d9", text="Donate", font=("Courier", 15), width=100,
                          command=donate)
        Button4 = Button(Frame1, background="#d9d9d9", text="Request", fg='black', font=("Courier", 15), width=100,
                         command=receive)
        Button4.place(relx=0.35, rely=0.49, height=53, width=100)
        Button4.configure()



def page():
    root.destroy()

    boot = Tk()
    boot.geometry("500x500+120+120")

    Label1 = Label(boot, text="Login_ID :")
    Label1.grid(row=2, column=2)
    l_id = Entry(boot)
    l_id.get()

    l_id.grid(row=2, column=3)
    Pass_Label = Label(boot, text="Password :")
    Pass_Label.grid(row=3, column=2)
    Password_box = Entry(boot, show="*")
    Password_box.grid(row=3, column=3)
    Password_box.get()
    Pass_Label1 = Label(boot, text=" Confirm Password :")
    Pass_Label1.grid(row=4, column=2)
    Password_box1 = Entry(boot, show="*")
    Password_box1.grid(row=4, column=3)
    Password_box1.get()
    l = Label(boot, text=" ")
    l.grid(row=5, column=0)
    Button_Submit = Button(boot, text="Login", padx=30, pady=10,
                           command=lambda: loginbut(l_id.get(), Password_box.get(), Password_box1.get(), boot))
    Button_Submit.grid(row=6, column=3)
