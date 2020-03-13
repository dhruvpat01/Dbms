from tkinter import *


def receive():
        t = Tk()

        t.title("Bloodbank/Receiver")

        t.geometry("500x300+120+120")

        name1 = Label(t, text="Enter Name")
        name1.grid(row=1, column=1)
        name2 = Entry(t)
        name2.grid(row=1, column=2)

        pname1 = Label(t, text="Enter Patient's Name")
        pname1.grid(row=2, column=1)
        pname2 = Entry(t)
        pname2.grid(row=2, column=2)

        psex = Label(t, text="Enter Sex Of the patient")
        psex.grid(row=3, column=1)
        v = StringVar(t, value="2")
        radiobutton1 = Radiobutton(t, text="Male", variable=v, value="Male")
        radiobutton1.grid(row=3, column=2)
        radiobutton2 = Radiobutton(t, text="Female", variable=v, value="Female")
        radiobutton2.grid(row=3, column=3)
        radiobutton3 = Radiobutton(t, text="Other", variable=v, value="Other")
        radiobutton3.grid(row=3, column=4)

        b = StringVar(t)
        pblood = Label(t, text="Enter Blood Group Required")
        pblood.grid(row=4, column=1)
        values = ["A Positive",
                  'A Negative',
                  'B Positive',
                  'B Negative',
                  'AB Positive',
                  'AB Negative',
                  'O Positive',
                  'O Negative']
        b.set('Select Blood Type')
        dropdown = OptionMenu(t, b, *values)
        dropdown.grid(row=4, column=2)

        Other1 = Label(t, text="If any other please specify")
        Other1.grid(row=5, column=1)
        Other2 = Entry(t)
        Other2.grid(row=5, column=2)

        page1 = Label(t, text="Enter Age")
        page1.grid(row=6, column=1)
        page2 = Entry(t)
        page2.grid(row=6, column=2)

        pamount1 = Label(t, text="Enter Amount of blood required in litres")
        pamount1.grid(row=6, column=1)
        pamount2 = Entry(t)
        pamount2.grid(row=6, column=2)

        number1 = Label(t, text="Enter Phone Number")
        number1.grid(row=7, column=1)
        number2 = Entry(t)
        number2.grid(row=7, column=2)

        anumber1 = Label(t, text="Enter Alternate Phone Number")
        anumber1.grid(row=7, column=1)
        anumber2 = Entry(t)
        anumber2.grid(row=7, column=2)

        t.mainloop()
