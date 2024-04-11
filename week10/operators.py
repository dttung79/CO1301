from tkinter import *
from tkinter import messagebox

##################### CREATE WINDOW  #####################
window = Tk()
window.title('Arithmetic Operators')
window.geometry('400x300')
##################### EVENT HANDLERS #####################
def btn_add_clicked():
    perform_op('+')
    
def btn_div_clicked():
    perform_op(':')

def perform_op(op='+'):
    try:
        a = int(txt_a.get())
        b = int(txt_b.get())
        if op == '+': c = a + b
        elif op == '-': c = a - b
        elif op == 'x': c = a * b
        elif op == ':': c = a / b

        txt_result.delete(0, END)
        txt_result.insert(0, f'{c}')
    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numbers')
    except ZeroDivisionError:
        messagebox.showerror('Error', 'Cannot divide by zero')
##################### CREATE WIDGETS #####################
lbl_a = Label(window, text='a:')
lbl_a.grid(row=0, column=0, padx=10)

txt_a = Entry(window, width=20)
txt_a.grid(row=0, column=1, columnspan=4, padx=5)

lbl_b = Label(window, text='b:')
lbl_b.grid(row=1, column=0, padx=10)

txt_b = Entry(window, width=20)
txt_b.grid(row=1, column=1, columnspan=4, padx=5)

btn_add = Button(window, text='+', command=btn_add_clicked)
btn_add.grid(row=2, column=1)
btn_sub = Button(window, text='-')
btn_sub.grid(row=2, column=2)
btn_mul = Button(window, text='x')
btn_mul.grid(row=2, column=3)
btn_div = Button(window, text=':', command=btn_div_clicked)
btn_div.grid(row=2, column=4)

txt_result = Entry(window, width=20)
txt_result.grid(row=3, column=1, columnspan=4, padx=5)
##################### RUN WINDOW     #####################
window.mainloop()