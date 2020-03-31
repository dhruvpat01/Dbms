from tkinter import *
from sqlite3 import *
from Fullscrn import *



def delet(d):
    obj4 = Tk()
    obj4.title("Delete page")
    Frame1 = Frame(obj4)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    delete1 = Button(Frame1, background="#d9d9d9", text="Delete User Records", fg='black', font=("Courier", 25), width=200, command=lambda :byemail(obj4))
    delete2 = Button(Frame1, background="#d9d9d9", text="Delete Donor Records", fg='black', font=("Courier", 25), width=300, command=lambda : byemail(obj4))
    delete3 = Button(Frame1, background="#d9d9d9", text="Delete Receiver Records", fg='black', font=("Courier", 25), width=200, command=lambda : byemail(obj4))
    delete4 = Button(Frame1, background="#d9d9d9", text="Delete Blood Inventory", fg='black', font=("Courier", 25), width=200, command=lambda : byblood(obj4))

    delete1.place(relx=0.35, rely=0.25, height=53, width=400)
    delete2.place(relx=0.35, rely=0.35, height=53, width=400)
    delete3.place(relx=0.35, rely=0.45, height=53, width=400)
    delete4.place(relx=0.35, rely=0.55, height=53, width=400)

    full11 = FullScreenApp(obj4)
    obj4.mainloop()

def byemail(a):
    a.destroy()
    d = Tk()
    d.title("Delete page")

    Frame1 = Frame(d)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    email1 = Label(Frame1)
    email1.place(relx=0.30, rely=0.45, height=33, width=200)
    email1.configure(background="#d9d9d9", text="Enter Email:", font=("Times", 10), width=1000)
    email2 = Entry(d)
    email2.place(relx=0.47, rely=0.45, height=33, width=200)

    delete1 = Button(Frame1, background="#d9d9d9", text="Delete", fg='black', font=("Times", 25), width=200)
    delete1.place(relx=0.47, rely=0.57, height=43, width=200)
    delete1.configure()

    full11=FullScreenApp(d)
    d.mainloop()

def byblood(a):
    a.destroy
    e = Tk()
    e.title("Delete page")

    Frame1 = Frame(e)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    email1 = Label(Frame1)
    email1.place(relx=0.30, rely=0.45, height=33, width=200)
    email1.configure(background="#d9d9d9", text="Enter Blood Group:", font=("Times", 10), width=1000)
    email2 = Entry(e)
    email2.place(relx=0.47, rely=0.45, height=33, width=200)

    delete1 = Button(Frame1, background="#d9d9d9", text="Delete", fg='black', font=("Times", 25), width=200)
    delete1.place(relx=0.47, rely=0.57, height=43, width=200)
    delete1.configure()

    full11 = FullScreenApp(e)
    e.mainloop()