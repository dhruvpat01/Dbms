import sqlite3
from tkinter import *
from Fullscrn import *
from Regsiter import *



def admin(b):
    obj = Tk()
    b.destroy()
    Frame1 = Frame(obj)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    create = Button(Frame1, background="#d9d9d9", text="Create", fg='black', font=("Courier", 25), width=200)
    show = Button(Frame1, background="#d9d9d9", text="Show Records", fg='black', font=("Courier", 20), width=300)
    update = Button(Frame1, background="#d9d9d9", text="Update", fg='black', font=("Courier", 25), width=200)
    delete = Button(Frame1, background="#d9d9d9", text="Delete", fg='black', font=("Courier", 25), width=200)

    label2 = Label(Frame1)
    label2.place(relx=0.35, rely=0.55, width=200)
    label2.configure(background="#d9d9d9", text="Any other SQL query", font="Times", width=1200)

    entry2 = Entry(Frame1)
    entry2.place(relx=0.55, rely=0.55, width=200)

    create.place(relx=0.45, rely=0.05, height=53, width=200)
    show.place(relx=0.45, rely=0.15, height=53, width=200)
    update.place(relx=0.45, rely=0.25, height=53, width=200)
    delete.place(relx=0.45, rely=0.35, height=53, width=200)

    full8 = FullScreenApp(obj)
    obj.mainloop()


