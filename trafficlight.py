from tkinter import *


light = Tk()
light.title("Traffic Light")
light.geometry("300x300")
light.config(background="black")

red_light = Button(light,text = "STOP", bg="red", width=20, height=5).place(x=80, y=20)
yellow_light = Button(light, text = "WAIT", bg="yellow", width=20, height=5).place(x=20, y=100)
green_light = Button(light, text = "GO", bg="green", width=20, height=5).place(x=80, y=180)


light.mainloop()