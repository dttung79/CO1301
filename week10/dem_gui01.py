from tkinter import *
def btn_swap_clicked():
    # get text from the labels
    text1 = lbl_hello.cget('text')
    text2 = lbl_python.cget('text')
    # reassign
    lbl_hello.config(text=text2)
    lbl_python.config(text=text1)

# create a window
window = Tk()
# set window title
window.title('Demo GUI 01')
# set window size
window.geometry('400x300') # width x height
# add a label
lbl_hello = Label(window, text='Hello, World!') # create a label, attach it to the window
# place the label in the window
lbl_hello.grid(row=0, column=0) # place the label in the first row and first column

btn_swap = Button(window, text='Swap', command=btn_swap_clicked)
btn_swap.grid(row=1, column=0)

# another label
lbl_python = Label(window, text='Python is fun!')
lbl_python.grid(row=2, column=0) 
# run the main loop
window.mainloop()