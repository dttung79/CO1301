from tkinter import *
from tkinter import messagebox

##################### CREATE WINDOW  #####################
window = Tk()
window.title('Book Store')
window.geometry('400x300')
##################### EVENT HANDLERS #####################
def btn_payment_clicked():
    try:
        price = float(txt_price.get())
        quant = int(txt_quantity.get())
        total = price * quant
        if cover_var.get() == True:
            total += 1 * quant
        if card_var.get() == True:
            total += 1.5 * quant

        total += delivery_var.get()
        
        messagebox.showinfo('Payment', f'Total payment: ${total}')
    except ValueError:
        messagebox.showerror('Error', 'Invalid input. Please enter numbers only.')
##################### CREATE WIDGETS #####################
lbl_book = Label(window, text='Book')
lbl_book.grid(row=0, column=0, padx=5, pady=5)

txt_book = Entry(window, width=20)
txt_book.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

lbl_price = Label(window, text='Price')
lbl_price.grid(row=1, column=0, padx=5, pady=5)

txt_price = Entry(window, width=20)
txt_price.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

lbl_quantity = Label(window, text='Quantity')
lbl_quantity.grid(row=2, column=0, padx=5, pady=5)

txt_quantity = Entry(window, width=20)
txt_quantity.grid(row=2, column=1, padx=5, pady=5, columnspan=2)

lbl_extra = Label(window, text='Extra')
lbl_extra.grid(row=3, column=0, padx=5, pady=5)

cover_var = BooleanVar()
cover_var.set(False)
chk_cover = Checkbutton(window, text='Cover ($1)', variable=cover_var)
chk_cover.grid(row=3, column=1, padx=5, pady=5, sticky=W)

card_var = BooleanVar()
card_var.set(False)
chk_card = Checkbutton(window, text='Card ($1.5)', variable=card_var)
chk_card.grid(row=3, column=2, padx=5, pady=5, sticky=E)

lbl_delivery = Label(window, text='Delivery')
lbl_delivery.grid(row=4, column=0, padx=5, pady=5)

delivery_var = IntVar()
delivery_var.set(0)
rd_normal = Radiobutton(window, text='Normal (Free)', variable=delivery_var, value=0)
rd_normal.grid(row=4, column=1, padx=5, pady=5, columnspan=2, sticky=W)
rd_express = Radiobutton(window, text='Express ($2)', variable=delivery_var, value=2)
rd_express.grid(row=5, column=1, padx=5, pady=5, columnspan=2, sticky=W)
rd_immediate = Radiobutton(window, text='Immediate ($5)', variable=delivery_var, value=5)
rd_immediate.grid(row=6, column=1, padx=5, pady=5, columnspan=2, sticky=W)

btn_payment = Button(window, text='Payment', command=btn_payment_clicked)
btn_payment.grid(row=7, column=1, columnspan=2, padx=5, pady=5, sticky=W)
##################### RUN WINDOW     #####################
window.mainloop()