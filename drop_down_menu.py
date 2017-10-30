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
edit_menu=Menu(menu)
menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Redo', command=donothing)
root.mainloop()
