from tkinter import *

name = Tk()
name.title("Name")
name.geometry("500x500")
name.config(background="lightblue")

label_name = Label(name, text="Enter Your Name:").place(x=50, y=80)
label_name_input = Entry(name, width=40).place(x=150, y=80)
submit_name_button = Button(name, text="Submit").place(x=200, y=120)

name.mainloop()
