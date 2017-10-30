from tkinter import *


def donothing():
    print('ok i wont')


root = Tk()
menu = Menu(root)
root.config(menu=menu)
submenu = Menu(menu)
menu.add_cascade(label='File', menu=submenu)
submenu.add_command(label='New Project...', command=donothing)
submenu.add_command(label='New', command=donothing)
submenu.add_separator()
submenu.add_command(label='Exit', command=root.quit)
edit_menu = Menu(menu)
menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Redo', command=donothing)

# **** Toolbar *****

toolbar = Frame(root, bg="blue")
insertBut = Button(toolbar, text="Insert Image", command=donothing)
insertBut.pack(side=LEFT, padx=2, pady=2)
print_but = Button(toolbar, text="Print", command=donothing)
print_but.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)
root.mainloop()
