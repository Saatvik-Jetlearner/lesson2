from tkinter import *

root = Tk()

root.geometry("100x100")

button = Button(root, text="Click Me", bd = "5", background="cyan", command=root.destroy)
button2 = Button(root, text="Click Me", bd = "5", background="green", command=root.destroy)

button.pack(side="right")
button2.pack(side="top")

root.mainloop()
