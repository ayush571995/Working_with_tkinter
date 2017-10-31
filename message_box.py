from tkinter import *
import tkinter.messagebox

root = Tk()
tkinter.messagebox.showinfo('Alert', 'Hi')
answer = tkinter.messagebox.askquestion('Quiz', 'Are you stupid?')
if answer == 'yes':
    print('yes you are')
else:
    print('you chose wrong option')
root.mainloop()
