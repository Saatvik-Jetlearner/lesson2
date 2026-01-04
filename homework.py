from tkinter import *
subscribe = Tk()
subscribe.geometry("400x200")
subscribe.config(background="lightblue")

ad = Label(subscribe, text="Subscribe to our Newsletter", font=("Arial", 16), bg="lightblue").place(x=80, y=20)
email = Label(subscribe, text="Email:", bg="lightblue").place(x=50, y=80)
email_input_area = Entry(subscribe, width=30).place(x=100, y=80)
submit_button = Button(subscribe, text="Subscribe").place(x=150, y=130)

subscribe.mainloop()