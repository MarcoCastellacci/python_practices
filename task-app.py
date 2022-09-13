from distutils.cmd import Command
import tkinter
from tkinter import ttk
from tkinter import Label
import random

window = tkinter.Tk()
window.title('Task Window')
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

def juego_num(resp):
    num = random()
    if num == resp:
        text_.config(text= 'You are a Mentalist')

num_entry = ttk.Entry(Command=juego_num())

num_entry.grid(row=0, column=0, padx=15, pady=15)


text_ = Label(window)
text_.grid()

window.mainloop()