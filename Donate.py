from tkinter import *
from Fullscrn import *

def donate(a):
    root2 = Tk()
    a.destroy()
    root2.geometry("500x500+120+120")
    root2.title("Blood Bank")
    root2.geometry("500x500+120+120")
    root2.configure(background="grey")


    Frame1 = Frame(root2)
    Frame1.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.96)
    Frame1.configure(borderwidth="2", background="#BD081C", width=500)

    label2 = Label(Frame1)
    label2.place(relx=0.10, rely=0.01, height=73, width=1000)
    label2.configure(background="#d9d9d9", text="Enter Donar Details", font=("Times", 25), width=1000)
    hospital_names = ["Manas Blood Bank", "Manas Blood Bank", "Pallavi Blood Bank", "Prabodhan Blood Bank",
                      "Ashirwad Blood Bank", "Blood Bank KEM"]


    name1 = Label(Frame1)
    name1.place(relx=0.25, rely=0.25, height=33, width=200)
    name1.configure(background="#d9d9d9", text="Enter Donar name", font=("Times", 10), width=1000)
    name1_entry = Entry(root2)
    name1_entry.get()
    name1_entry.place(relx=0.42, rely=0.26, height=33, width=200)

    age = Label(Frame1)
    age.place(relx=0.25, rely=0.35, height=33, width=200)
    age.configure(background="#d9d9d9", text="Enter Age", font=("Times", 10), width=1000)
    age_entry = Entry(root2)
    age_entry.get()
    age_entry.place(relx=0.42, rely=0.35, height=33, width=200)

    psex = Label(Frame1)
    psex.place(relx=0.25, rely=0.45, height=33, width=200)
    psex.configure(background="#d9d9d9", text="Select Sex of Donor ", font=("Times", 10))
    v = StringVar(root2, value="0")
    radiobutton1 = Radiobutton(Frame1, text="Male", variable=v, value="Male", font=("Times", 10))
    radiobutton1.place(relx=0.45, rely=0.45)
    radiobutton2 = Radiobutton(Frame1, text="Female", variable=v, value="Female", font=("Times", 10))
    radiobutton2.place(relx=0.55, rely=0.45)
    radiobutton3 = Radiobutton(Frame1, text="Other", variable=v, value="Other", font=("Times", 10))
    radiobutton3.place(relx=0.65, rely=0.45)

    b = StringVar(Frame1)
    pblood = Label(root2, text="Select Your Blood Group ")
    pblood.configure(background="#d9d9d9", font=("Times", 10))
    pblood.place(relx=0.26, rely=0.57, height=33, width=200)
    values = ["A Positive",
              'A Negative',
              'B Positive',
              'B Negative',
              'AB Positive',
              'AB Negative',
              'O Positive',
              'O Negative']
    b.set('Select Your Blood Type')
    dropdown = OptionMenu(root2, b, *values)
    dropdown.place(relx=0.42, rely=0.57, height=33, width=200)

    var = StringVar(Frame1)
    slect_names = Label(root2, text="Selec Blood Bank")
    slect_names.configure(background="#d9d9d9", font=("Times", 10))
    slect_names.place(relx=0.26, rely=0.67, height=33, width=200)
    var.set('Blood Bank Names')
    select = OptionMenu(root2, var, *hospital_names)
    select.place(relx=0.42, rely=0.67, height=33, width=200)

    Button_Submit = Button(Frame1, text="Submit", padx=30, pady=10, font=("Times", 20))
    Button_Submit.place(relx=0.35, rely=0.84, height=45, width=300)

    full5=FullScreenApp(root2)
    root2.mainloop()
