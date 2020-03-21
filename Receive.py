from tkinter import *
from Fullscrn import *

def receive(a):
    t = Tk()
    a.destroy()
    t.title("Blood Bank")
    t.geometry("500x500+120+120")
    t.configure(background="grey")
    Frame1 = Frame(t)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    name1 = Label(Frame1)
    name1.place(relx=0.25, rely=0.05, height=33, width=200)
    name1.configure(background="#d9d9d9", text="Enter name", font=("Times", 10), width=1000)
    name2 = Entry(t)
    name2.get()
    name2.place(relx=0.42, rely=0.07, height=33, width=200)


    pname1 = Label(Frame1)
    pname1.place(relx=0.25, rely=0.15, height=33, width=200)
    pname1.configure(background="#d9d9d9", text="Enter Patient  name", font=("Times", 10), width=200)
    pname2 = Entry(t)
    pname2.get()
    pname2.place(relx=0.42, rely=0.17, height=33, width=500)

    psex = Label(Frame1)
    psex.place(relx=0.25, rely=0.25, height=33, width=200)
    psex.configure(background="#d9d9d9", text="Select Sex of Patient ", font=("Times", 10))
    v = StringVar(t, value="0")
    radiobutton1 = Radiobutton(Frame1, text="Male", variable=v, value="Male",font=("Times", 10))
    radiobutton1.place(relx=0.45, rely=0.27)
    radiobutton2 = Radiobutton(Frame1, text="Female", variable=v, value="Female",font=("Times", 10))
    radiobutton2.place(relx=0.55, rely=0.27)
    radiobutton3 = Radiobutton(Frame1, text="Other", variable=v, value="Other",font=("Times", 10))
    radiobutton3.place(relx=0.65, rely=0.27)

    b = StringVar(Frame1)
    pblood = Label(t, text="Select Blood Group Required")
    pblood.configure(background="#d9d9d9",font=("Times", 10))
    pblood.place(relx=0.26, rely=0.37,height=33,width=200)
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
    dropdown.place(relx=0.42, rely=0.37,height=33,width=200)
    Other1 = Label(Frame1)
    Other1.place(relx=0.25, rely=0.43, height=33, width=200)
    Other1.configure(background="#d9d9d9", text="If any other please specify" , font=("Times", 10))
    Other2 = Entry(t)
    Other2.get()
    Other2.place(relx=0.42, rely=0.43, height=33, width=200)

    page1 = Label(Frame1)
    page1.place(relx=0.25, rely=0.52, height=33, width=200)
    page1.configure(background="#d9d9d9", text="Enter Age", font=("Times", 10))
    page2 = Entry(t)
    page2.get()
    page2.place(relx=0.42, rely=0.52, height=33, width=200)

    pamount1 = Label(Frame1)
    pamount1.place(relx=0.25, rely=0.65, height=33, width=200)
    pamount1.configure(background="#d9d9d9", text="Enter Amount of blood required in litres", font=("Times", 8))
    pamount2 = Entry(t)
    pamount2.get()
    pamount2.place(relx=0.42, rely=0.63, height=33, width=200)

    number1 = Label(Frame1)
    number1.place(relx=0.25, rely=0.75, height=33, width=200)
    number1.configure(background="#d9d9d9", text="Enter Phone Number", font=("Times", 10))
    number2 = Entry(t)
    number2.get()
    number2.place(relx=0.42, rely=0.72, height=33, width=200)

    anumber1 = Label(Frame1)
    anumber1.place(relx=0.25, rely=0.85, height=33, width=200)
    anumber1.configure(background="#d9d9d9", text="Enter Alternate Phone Number", font=("Times", 10))
    anumber2 = Entry(t)
    anumber2.get()
    anumber2.place(relx=0.42, rely=0.82, height=33, width=200)

    Button_Submit = Button(Frame1, text="Submit", padx=30, pady=10, font=("Times", 20))
    Button_Submit.place(relx=0.35, rely=0.92, height=45, width=300)
    full4=FullScreenApp(t)
    t.mainloop()