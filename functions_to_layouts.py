from tkinter import *

root = Tk()


def print_name(event):
    print("Hello my name is ayush Saluja")

button_1 = Button(root, text="Print Name")
button_1.bind("<Button-1>", print_name)
button_1.pack()
root.mainloop()
