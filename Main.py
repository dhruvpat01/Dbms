from Regsiter import *
from tkinter import *

root = Tk()


class blood_bank:
    def __init__(self):
        root.geometry("963x749+540+110")
        root.title("Blood Bank")
        root.configure(background="#d9d9d9")

        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(borderwidth="2", background="#BD081C", width=925)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.65, rely=0.69, height=103, width=400)
        self.Button3.configure(background="#d9d9d9", text="Login", font=("Courier", 35), width=400, command=lambda :page(root))
        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.65, rely=0.49, height=103, width=400)
        self.Button4.configure(background="#d9d9d9", text="Register", font=("Courier", 35), width=400, command=lambda :register(root))

        root.mainloop()


if __name__ == '__main__':
    user = blood_bank()
