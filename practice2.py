from tkinter import *

details = Tk()
details.title("User Details Form")
details.geometry("500x500")
details.config(background="lightblue")

first_name_details = Label(details, text="First Name:").place(x=40, y=60)
first_name_input = Entry(details, width=30).place(x=110, y=60)

age_details = Label(details, text="Age:").place(x=40, y=100)
age_input = Entry(details, width=30).place(x=110, y=100)

city_details = Label(details, text="City:").place(x=40, y=140)
city_input = Entry(details, width=30).place(x=110, y=140)

submit_button = Button(details, text="Submit").place(x=40, y=180)
clear_button = Button(details, text="Clear").place(x=100, y=180)

details.mainloop()