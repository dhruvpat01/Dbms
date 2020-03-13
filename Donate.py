from tkinter import *


def donate(a):

        root2=Tk()
        a.destroy()
        root2.geometry("500x500+120+120")
        hospital_names = ["Manas Blood Bank","Manas Blood Bank","Pallavi Blood Bank","Prabodhan Blood Bank","Ashirwad Blood Bank","Blood Bank KEM"]
        variable=StringVar()

        name1 = Label(root2, text="Enter First Name").grid(row=0, column=0)
        name1_entry = Entry(root2).grid(row=0, column=1)
        name2= Label(root2, text="Enter Second Name").grid(row=1, column=0)
        name2_entry = Entry(root2).grid(row=1, column=1)

        age = Label(root2, text="Enter Age").grid(row=2, column=0)
        age_entry = Entry(root2).grid(row=2, column=1)
        sex = Label(root2, text="Enter Sex").grid(row=3, column=0)
        sex_entry = Entry(root2).grid(row=3, column=1)
        blood = Label(root2, text="Enter Blood Group").grid(row=3, column=0)
        blood_entry = Entry(root2).grid(row=3, column=1)
        slect_names = Label(root2, text="Selec Blood Bank").grid(row=4, column=0)
        select = OptionMenu(root2, variable, *hospital_names)
        variable.set("Blood Bank Names")
        select.grid(row=4, column=1)

        root2.mainloop()