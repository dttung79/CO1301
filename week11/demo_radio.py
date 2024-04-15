from tkinter import *
from tkinter import messagebox

##################### CREATE WINDOW  #####################
window = Tk()
window.title('Demo Radio Buttons')
window.geometry('400x300')
##################### EVENT HANDLERS #####################
def language_selected():
    if language.get() == 0:
        lbl_message.config(text='I love Python')
    elif language.get() == 1:
        lbl_message.config(text='I love Java')
    elif language.get() == 2:
        lbl_message.config(text='I love C#')
        
##################### CREATE WIDGETS #####################
language = IntVar()
language.set(0)

rd_python = Radiobutton(window, text='Python', variable=language, value=0, command=language_selected)
rd_python.grid(row=0, column=0)

rd_java = Radiobutton(window, text='Java', variable=language, value=1, command=language_selected)
rd_java.grid(row=0, column=1)

rd_csharp = Radiobutton(window, text='C#', variable=language, value=2, command=language_selected)
rd_csharp.grid(row=0, column=2)

lbl_message = Label(window, text='I love Python')
lbl_message.grid(row=1, column=0, columnspan=3, sticky=W, padx=5, pady=10)


##################### RUN WINDOW     #####################
window.mainloop()