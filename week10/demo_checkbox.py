from tkinter import *
from tkinter import messagebox

##################### CREATE WINDOW  #####################
window = Tk()
window.title('Arithmetic Operators')
window.geometry('400x300')
##################### EVENT HANDLERS #####################
def chk_demo_checked():
    if demo_var.get() == True:
        lbl_status.config(text='Status: Checked')
    else:
        lbl_status.config(text='Status: Unchecked')
##################### CREATE WIDGETS #####################
demo_var = BooleanVar()
demo_var.set(True)
chk_demo = Checkbutton(window, text='Checkbutton Demo', variable=demo_var, command=chk_demo_checked)
chk_demo.grid(row=0, column=0, sticky=W)

lbl_status = Label(window, text='Status: Checked')
lbl_status.grid(row=1, column=0, sticky=W)
##################### RUN WINDOW     #####################
window.mainloop()