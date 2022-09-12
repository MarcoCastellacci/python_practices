import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

def buttonSelected():
    print(f'The selected button is')

buttons = tkinter.StringVar()
radio_button1 = ttk.Radiobutton(window, text="Radio Button 1", value=1, variable=buttons, command=buttonSelected)
radio_button2 = ttk.Radiobutton(window, text="Radio Button 2", value=2, variable=buttons, command=buttonSelected)
radio_button3 = ttk.Radiobutton(window, text="Radio Button 3", value=3, variable=buttons, command=buttonSelected)

radio_button1.grid(row=0,column=0, padx=5, pady=5)
radio_button2.grid(row=0,column=1, padx=5, pady=5)
radio_button3.grid(row=0,column=2, padx=5, pady=5)


window.mainloop()