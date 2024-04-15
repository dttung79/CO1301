from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

##################### CREATE WINDOW  #####################
window = Tk()
window.title('Demo Combo Box')
window.geometry('400x300')
##################### EVENT HANDLERS #####################
def cbb_language_selected(event):
    if cbb_language.get() == 'Python':
        lbl_message.config(text='Python is good for data science')
    elif cbb_language.get() == 'Java':
        lbl_message.config(text='Java is good for enterprise applications')
    elif cbb_language.get() == 'C#':
        lbl_message.config(text='C# is good for game development')
        
##################### CREATE WIDGETS #####################
cbb_language = Combobox(window, values=['Python', 'Java', 'C#'])
cbb_language.grid(row=0, column=0, padx=5, pady=5)
cbb_language.current(0) # set the default value is Python
cbb_language.bind('<<ComboboxSelected>>', cbb_language_selected)

lbl_message = Label(window, text='Choose your favorite language')
lbl_message.grid(row=1, column=0, padx=5, pady=5)
##################### RUN WINDOW     #####################
window.mainloop()