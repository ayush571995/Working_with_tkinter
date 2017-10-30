from tkinter import *

root = Tk()
# theLabel = Label(root, text="This is too easy")
# theLabel.pack()
top = Frame(root)
top.pack()
bottom = Frame(root)
bottom.pack(side=BOTTOM)

button1 = Button(top, text="Button 1", fg="red")
button2 = Button(top, text="Button 2", fg="blue")
button3 = Button(top, text="Button 3", fg="green")
button4 = Button(bottom, text="Button 4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()
