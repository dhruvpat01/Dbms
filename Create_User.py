from tkinter import *
from sqlite3 import *
from Fullscrn import *

def Create_User(a):
    toot = Tk()
    name2 = StringVar()
    page2 = IntVar()
    l_id = StringVar()
    Password_box = StringVar()
    a.destroy()
    toot.title("Create User")
    toot.geometry("500x500+120+120")
    toot.configure(background="grey")

    Frame1 = Frame(toot)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    label2 = Label(Frame1)
    label2.place(relx=0.10, rely=0.01, height=73, width=1000)
    label2.configure(background="#d9d9d9", text="Create New User", font=("Times", 25), width=1000)

    name1 = Label(Frame1)
    name1.place(relx=0.30, rely=0.15, height=33, width=200)
    name1.configure(background="#d9d9d9", text="Enter Name:", font=("Times", 10), width=1000)
    name2 = Entry(toot)
    name2.place(relx=0.47, rely=0.16, height=33, width=200)

    psex = Label(Frame1)
    psex.place(relx=0.25, rely=0.25, height=33, width=200)
    psex.configure(background="#d9d9d9", text="Select Sex of Patient ", font=("Times", 10))
    v = StringVar(Frame1, value="ale")
    radiobutton1 = Radiobutton(Frame1, text="Male", variable=v, value="Male", font=("Times", 10))
    radiobutton1.place(relx=0.45, rely=0.25)
    radiobutton2 = Radiobutton(Frame1, text="Female", variable=v, value="Female", font=("Times", 10))
    radiobutton2.place(relx=0.55, rely=0.25)
    radiobutton3 = Radiobutton(Frame1, text="Other", variable=v, value="Other", font=("Times", 10))
    radiobutton3.place(relx=0.65, rely=0.25)

    page1 = Label(Frame1)
    page1.place(relx=0.30, rely=0.35, height=33, width=200)
    page1.configure(background="#d9d9d9", text="Enter Age:", font=("Times", 10))
    page2 = Entry(toot)
    page2.place(relx=0.47, rely=0.35, height=33, width=200)

    phonenumber1 = Label(Frame1)
    phonenumber1.place(relx=0.30, rely=0.45, height=33, width=200)
    phonenumber1.configure(background="#d9d9d9", text="Enter Phone Number:", font=("Times", 10), width=1000)
    phonenumber2 = Entry(toot)
    phonenumber2.place(relx=0.47, rely=0.46, height=33, width=200)

    Label1 = Label(Frame1)
    Label1.place(relx=0.30, rely=0.55, height=33, width=200)
    Label1.configure(background="#d9d9d9", text=" Set Login_ID/Email_ID :", font=("Times", 10), width=1000)
    l_id = Entry(toot)
    l_id.place(relx=0.47, rely=0.54, height=33, width=200)

    Pass_Label1 = Label(Frame1)
    Pass_Label1.place(relx=0.30, rely=0.65, height=33, width=200)
    Pass_Label1.configure(background="#d9d9d9", text=" Set Password: ", font=("Times", 10), width=1000)
    Password_box = Entry(toot, show="*")
    Password_box.place(relx=0.47, rely=0.63, height=33, width=200)

    Pass_Label1 = Label(Frame1)
    Pass_Label1.place(relx=0.30, rely=0.75, height=33, width=200)
    Pass_Label1.configure(background="#d9d9d9", text=" Confirm Password ", font=("Times", 10), width=1000)
    Password_box1 = Entry(toot, show="*")
    Password_box1.place(relx=0.47, rely=0.73, height=33, width=200)

    full12=FullScreenApp(toot)
    toot.mainloop()