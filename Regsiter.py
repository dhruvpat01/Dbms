# from tkinter import *
# from tkinter import ttk
from tkinter import messagebox

from Login import *



def register(a):
    loot = Tk()
    a.destroy()
    loot.geometry("500x500+120+120")
    empty = Label(loot, text=" ")
    empty.grid(row=0)
    name1 = Label(loot, text="Enter Name")
    name1.grid(row=1, column=1)
    name2 = Entry(loot)
    name2.grid(row=1, column=2)
    psex = Label(loot, text="Enter Sex Of the patient")
    psex.grid(row=3, column=1)
    v = StringVar(loot, value="2")
    radiobutton1 = Radiobutton(loot, text="Male", variable=v, value="Male")
    radiobutton1.grid(row=3, column=2)
    radiobutton2 = Radiobutton(loot, text="Female", variable=v, value="Female")
    radiobutton2.grid(row=3, column=3)
    radiobutton3 = Radiobutton(loot, text="Other", variable=v, value="Other")
    radiobutton3.grid(row=3, column=4)
    page1 = Label(loot, text="Enter Age")
    page1.grid(row=4, column=1)
    page2 = Entry(loot)
    page2.grid(row=4, column=2)
    Label1 = Label(loot, text="Login_ID/Email_ID :")
    Label1.grid(row=5, column=1)
    l_id = Entry(loot)
    l_id.get()

    l_id.grid(row=5, column=2)
    Pass_Label = Label(loot, text="Password :")
    Pass_Label.grid(row=6, column=1)
    Password_box = Entry(loot, show="*")
    Password_box.grid(row=6, column=2)
    Password_box.get()
    Pass_Label1 = Label(loot, text=" Confirm Password :")
    Pass_Label1.grid(row=7, column=1)
    Password_box1 = Entry(loot, show="*")
    Password_box1.grid(row=7, column=2)
    Button_Submit = Button(loot, text="Register", padx=30, pady=10,
                           command=lambda: loginbob(name2.get(), page2.get(), l_id.get(), Password_box.get(),
                                                    Password_box1.get(), loot))
    Button_Submit.grid(row=8, column=2)

    def loginbob(l, n, a, b, c, d):
        if not (re.search("[A-Za-z_ ]", l)):
            r = messagebox.showerror("popup", "Name should only contain character")

        elif not (re.search("\d", n)):
            q = messagebox.showerror("popup", "only integer is valid")

        elif not (re.search("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", a)):
            d = messagebox.showwarning("popup", "email is invalid")

        elif not (re.search("[\w@$&_!]{8,14}", b)):
            e = messagebox.showwarning("popup", "password is weak or too short")


        elif not (c == b):
            a = messagebox.showwarning("popup", "your passwords do not match")
        else:
            root1 = Tk()
            d.destroy()
            root1.title("Blood Bank")
            root1.geometry("500x500+120+120")
            root1.configure(background="grey")
            Frame1 = Frame(root1)
            Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
            Frame1.configure(borderwidth="2", background="grey", width=500)

            Button3 = Button(Frame1)
            Button3.place(relx=0.35, rely=0.69, height=53, width=100)
            Button3.configure(background="#d9d9d9", text="Donate", font=("Courier", 15), width=100,
                              command=lambda: donate(root1))
            Button4 = Button(Frame1, background="#d9d9d9", text="Request", fg='black', font=("Courier", 15), width=100,
                             command=lambda: receive(root1))
            Button4.place(relx=0.35, rely=0.49, height=53, width=100)
            Button4.configure()
