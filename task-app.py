from distutils.cmd import Command
from multiprocessing import Value
import tkinter
from tkinter import ttk
from tkinter import Label
import random

window = tkinter.Tk()
window.title('Task Window')
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
text_ = Label(window)

def juego_num(resp):
    num = random.randint(0,100)
    if num < resp:
        text_.config(text= 'Your Number is Bigger')
    elif num > resp:    
        text_.config(text= 'Your Number is Smaller')
    else:
        text_.config(text= 'Your Number is Correct')    
        
num = tkinter.IntVar()
num_obtenido = int(num.get())
num_entry = ttk.Entry(textvariable=num)
res_button = ttk.Button(window, text='Start Play', command=juego_num(num_obtenido))


num_entry.grid(row=0, column=0, padx=15, pady=15)
res_button.grid(row=1, column=0, padx=5, pady=5)


text_.grid()

window.mainloop()