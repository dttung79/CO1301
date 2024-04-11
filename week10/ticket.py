from tkinter import *
from tkinter import messagebox

##################### CREATE WINDOW  #####################
window = Tk()
window.title('Airline Ticket Payment')
window.geometry('400x300')
##################### EVENT HANDLERS #####################
def btn_payment_clicked():
    try:
        # get the number of tickets
        n_tickets = int(txt_tickets.get())
        # get the price of each ticket
        price = float(txt_price.get())
        payment = price * n_tickets

        if baggage_var.get() == True:
            payment += 5 * n_tickets
        if lunch_var.get() == True:
            payment += 3 * n_tickets
        
        lbl_payment.config(text=f'${payment}')
    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numbers')

##################### CREATE WIDGETS #####################
lbl_tickets = Label(window, text='Number of tickets:')
lbl_tickets.grid(row=0, column=0, padx=5, sticky=E)

txt_tickets = Entry(window, width=20)
txt_tickets.grid(row=0, column=1, padx=5, sticky=W)

lbl_price = Label(window, text='Price:')
lbl_price.grid(row=1, column=0, padx=5, sticky=E)

txt_price = Entry(window, width=20)
txt_price.grid(row=1, column=1, padx=5, sticky=W)

lbl_extras = Label(window, text='Extra service:')
lbl_extras.grid(row=2, column=0, padx=5, sticky=E)

baggage_var = BooleanVar()
chk_baggage = Checkbutton(window, text='Baggage ($5)', variable=baggage_var)
chk_baggage.grid(row=2, column=1, padx=5, sticky=W)

lunch_var = BooleanVar()
chk_lunch = Checkbutton(window, text='Lunch ($3)', variable=lunch_var)
chk_lunch.grid(row=3, column=1, padx=5, sticky=W)

btn_payment = Button(window, text='Payment', command=btn_payment_clicked)
btn_payment.grid(row=4, column=0, padx=5, sticky=E)

lbl_payment = Label(window, text='$0')
lbl_payment.grid(row=4, column=1, padx=5, sticky=W)
##################### RUN WINDOW     #####################
window.mainloop()