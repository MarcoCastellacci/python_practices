import tkinter
from tkinter import ttk
from tkinter import Label

window = tkinter.Tk()
window.title('Task Window')
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

buttons = tkinter.StringVar()
texto= tkinter.StringVar()

def buttonSelected():
    selected= "Your Selection is " + buttons.get()
    text_selected.config(text=selected)
    print(buttons.get())
    
def mostrartexto():
    inputText= "Your Name is " + texto.get()
    name_user.config(text=inputText)
    print(texto.get())    

def restart():
    buttons.set(None)
    texto.set('')
    text_selected.config(text="")
    name_user.config(text="")

radio_button1 = ttk.Radiobutton(window, text="Radio Button 1", value=1, variable=buttons, command=buttonSelected)
radio_button2 = ttk.Radiobutton(window, text="Radio Button 2", value=2, variable=buttons, command=buttonSelected)
radio_button3 = ttk.Radiobutton(window, text="Radio Button 3", value=3, variable=buttons, command=buttonSelected)

clear_button = ttk.Button(window, text='Clear Selection', command=restart)
username= ttk.Entry(window, text='Put your Name', textvariable=texto )
ok_button= ttk.Button(window, text='OK', command=mostrartexto)

radio_button1.grid(row=0,column=0, padx=5, pady=5)
radio_button2.grid(row=0,column=1, padx=5, pady=5)
radio_button3.grid(row=0,column=2, padx=5, pady=5)
clear_button.grid(row=1, column=0, padx=5, pady=5)
username.grid(row=2, column=1, pady=20, padx=20)
ok_button.grid(row=3, column=0, padx=5, pady=5)



name_user = Label(window)
text_selected = Label(window)
text_selected.grid()
name_user.grid()

window.mainloop()