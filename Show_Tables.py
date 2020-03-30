from tkinter import *
from sqlite3 import *
from Fullscrn import *

def sho(b):
    obj5 = Tk()
    obj5.title("Show page")
    Frame1 = Frame(obj5)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    show1 = Button(Frame1, background="#d9d9d9", text="Show User Table", fg='black', font=("Courier", 25), width=200)
    show2 = Button(Frame1, background="#d9d9d9", text="Show Donor Table", fg='black', font=("Courier", 25), width=300)
    show3 = Button(Frame1, background="#d9d9d9", text="Show Receiver Table", fg='black', font=("Courier", 25), width=200)
    show4 = Button(Frame1, background="#d9d9d9", text="Show Blood Inventory", fg='black', font=("Courier", 25), width=200)

    show1.place(relx=0.35, rely=0.25, height=53, width=400)
    show2.place(relx=0.35, rely=0.35, height=53, width=400)
    show3.place(relx=0.35, rely=0.45, height=53, width=400)
    show4.place(relx=0.35, rely=0.55, height=53, width=400)


    full11 = FullScreenApp(obj5)
    obj5.mainloop()
