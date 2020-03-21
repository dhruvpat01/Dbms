# from tkinter import *
# from tkinter import ttk
from tkinter import messagebox

from Login import *

from Fullscrn import *

def register(a):
    loot = Tk()
    a.destroy()
    loot.title("Blood Bank")
    loot.geometry("500x500+120+120")
    loot.configure(background="grey")
    Frame1 = Frame(loot)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    label2 = Label(Frame1)
    label2.place(relx=0.10, rely=0.01, height=73, width=1000)
    label2.configure(background="#d9d9d9", text="Registration Form", font=("Times", 25), width=1000)
    l_id = Entry(loot)
    name1 = Label(Frame1)
    name1.place(relx=0.25, rely=0.15, height=33, width=200)
    name1.configure(background="#d9d9d9", text="Enter name", font=("Times", 10), width=1000)
    name2 = Entry(loot)
    name2.get()
    name2.place(relx=0.42, rely=0.16, height=33, width=200)

    pname1 = Label(Frame1)
    pname1.place(relx=0.25, rely=0.25, height=33, width=200)
    pname1.configure(background="#d9d9d9", text="Enter Patient  name", font=("Times", 10), width=1000)
    pname2 = Entry(loot)
    pname2.get()
    pname2.place(relx=0.42, rely=0.26, height=33, width=200)

    psex = Label(Frame1)
    psex.place(relx=0.25, rely=0.35, height=33, width=200)
    psex.configure(background="#d9d9d9", text="Enter Sex of Patient ", font=("Times", 10))
    v = StringVar(loot, value="0")
    radiobutton1 = Radiobutton(Frame1, text="Male", variable=v, value="Male", font=("Times", 10))
    radiobutton1.place(relx=0.45, rely=0.35)
    radiobutton2 = Radiobutton(Frame1, text="Female", variable=v, value="Female", font=("Times", 10))
    radiobutton2.place(relx=0.55, rely=0.35)
    radiobutton3 = Radiobutton(Frame1, text="Other", variable=v, value="Other", font=("Times", 10))
    radiobutton3.place(relx=0.65, rely=0.35)

    page1 = Label(Frame1)
    page1.place(relx=0.25, rely=0.45, height=33, width=200)
    page1.configure(background="#d9d9d9", text="Enter Age", font=("Times", 10))
    page2 = Entry(loot)
    page2.get()
    page2.place(relx=0.42, rely=0.44, height=33, width=200)

    Label1 = Label(Frame1)
    Label1.place(relx=0.25, rely=0.55, height=33, width=200)
    Label1.configure(background="#d9d9d9", text=" Set Login_ID/Email_ID :", font=("Times", 10), width=1000)
    l_id = Entry(loot)
    l_id.get()
    l_id.place(relx=0.42, rely=0.54, height=33, width=200)

    Pass_Label1 = Label(Frame1)
    Pass_Label1.place(relx=0.25, rely=0.65, height=33, width=200)
    Pass_Label1.configure(background="#d9d9d9", text=" Set Password ", font=("Times", 10), width=1000)
    Password_box= Entry(loot,show="*")
    Password_box.get()
    Password_box.place(relx=0.42, rely=0.63, height=33, width=200)

    Pass_Label1 = Label(Frame1)
    Pass_Label1.place(relx=0.25, rely=0.75, height=33, width=200)
    Pass_Label1.configure(background="#d9d9d9", text=" Confirm Password ", font=("Times", 10), width=1000)
    Password_box1 = Entry(loot, show="*")
    Password_box1.get()
    Password_box1.place(relx=0.42, rely=0.73, height=33, width=200)

    Button_Submit = Button(Frame1, text="Register", padx=30, pady=10,font=("Times", 20),
                           command=lambda: loginbob(name2.get(), page2.get(), l_id.get(), Password_box.get(),
                                                    Password_box1.get(), loot))
    Button_Submit.place(relx=0.35, rely=0.84, height=45, width=300)
    full3=FullScreenApp(loot)
    loot.mainloop()


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
            full6=FullScreenApp(root1)
            root1.mainloop()