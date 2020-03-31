from tkinter import *
from sqlite3 import *
import sqlite3
from Fullscrn import *

def sho(b):
    obj5 = Tk()
    obj5.title("Show page")
    Frame1 = Frame(obj5)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    show1 = Button(Frame1, background="#d9d9d9", text="Show User Table", fg='black', font=("Courier", 25), width=200,command=lambda :User(obj5))
    show2 = Button(Frame1, background="#d9d9d9", text="Show Donor Table", fg='black', font=("Courier", 25), width=300)
    show3 = Button(Frame1, background="#d9d9d9", text="Show Receiver Table", fg='black', font=("Courier", 25), width=200)
    show4 = Button(Frame1, background="#d9d9d9", text="Show Blood Inventory", fg='black', font=("Courier", 25), width=200)

    show1.place(relx=0.35, rely=0.25, height=53, width=400)
    show2.place(relx=0.35, rely=0.35, height=53, width=400)
    show3.place(relx=0.35, rely=0.45, height=53, width=400)
    show4.place(relx=0.35, rely=0.55, height=53, width=400)


    full11 = FullScreenApp(obj5)
    obj5.mainloop()


conn = sqlite3.connect("Blood_Bank.db")
c = conn.cursor()
def User(r):
    l=Tk()

    c.execute("SELECT * FROM User")
    records=c.fetchall()
    Frame1 = Frame(l)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)
    Label1 = Label(Frame1)
    Label1.place(relx=0.30, rely=0.55, height=33, width=200)
    Label1.configure(background="#d9d9d9", text=" UserTable :", font=("Times", 10), width=1000)

    print_records=" "
    for record in records:
        print_records+=str(record)+"\n"
    querry_label=Label(Frame1)

    querry_label.configure(background="#d9d9d9", text=print_records, font=("Times", 10), width=1000)
    querry_label.pack()

    conn.commit()
    conn.close()
    full11 = FullScreenApp(l)
    l.mainloop()

