from tkinter import *
from Donate import *
from Receive import *
from Main import *

def abc():
    receive()

class nextpage:
        def __init__(self):
            root1 = Tk()
            root1.title("Blood Bank")
            root1.geometry("400x400")
            root1.configure(background="grey")
            self.Frame1 = Frame(root1)
            self.Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
            self.Frame1.configure(borderwidth="2", background="grey", width=500)

            self.Button3 = Button(self.Frame1)
            self.Button3.place(relx=0.35, rely=0.69, height=53, width=100)
            self.Button3.configure(background="#d9d9d9", text="Donate", font=("Courier", 15), width=100,command=donate)
            self.Button4 = Button(self.Frame1)
            self.Button4.place(relx=0.35, rely=0.49, height=53, width=100)
            self.Button4.configure(background="#d9d9d9", text="Request", font=("Courier", 15), width=100,command=receive)



            root1.mainloop()
