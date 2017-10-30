from tkinter import *


def left_click(event):
    print("Left")


def right_click(event):
    print("right")

#
# def middle_click(event):
#     print("middle")


root = Tk()
frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", left_click)
frame.bind('<Button-3>', right_click)
frame.pack()
root.mainloop()
