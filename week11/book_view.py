from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import filedialog
import csv
##################### CREATE WINDOW  #####################
window = Tk()
window.title('Book View')
window.geometry('400x300')
##################### EVENT HANDLERS #####################
def load_books():
    file_name = filedialog.askopenfilename()
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        row = next(reader) # skip header
        titles = []
        prices = []
        authors = []
        for row in reader:
            titles.append(row[0])
            prices.append(row[1])
            authors.append(row[2])
        '''this is a comment'''
        return titles, prices, authors

def cbb_books_selected(event):
    # get selected index
    index = cbb_books.current()
    price = prices[index]
    author = authors[index]
    txt_price.delete(0, END)
    txt_price.insert(0, price)
    txt_author.delete(0, END)
    txt_author.insert(0, author)
##################### CREATE WIDGETS #####################
lbl_book = Label(window, text='Book')
lbl_book.grid(row=0, column=0, padx=5, pady=5, sticky=E)

titles, prices, authors = load_books()
cbb_books = Combobox(window, values=titles)
cbb_books.grid(row=0, column=1, padx=5, pady=5, sticky=W)
cbb_books.current(0) # selecte the 1st book
cbb_books.bind('<<ComboboxSelected>>', cbb_books_selected)

lbl_price = Label(window, text='Price')
lbl_price.grid(row=1, column=0, padx=5, pady=5, sticky=E)

txt_price = Entry(window, width=20)
txt_price.grid(row=1, column=1, padx=5, pady=5, sticky=W)

lbl_author = Label(window, text='Author')
lbl_author.grid(row=2, column=0, padx=5, pady=5, sticky=E)

txt_author = Entry(window, width=20)
txt_author.grid(row=2, column=1, padx=5, pady=5, sticky=W)
##################### RUN WINDOW     #####################
window.mainloop()