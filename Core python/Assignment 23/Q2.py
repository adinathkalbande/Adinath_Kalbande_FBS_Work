# Build a currency converter application that converts between different currencies. The
# user should be able to enter an amount, select the input currency, select the output
# currency, and see the converted amount.

from tkinter import *
from tkinter import messagebox

def changeCurrency():
    amount = float(currency_entry.get())
    value = x.get()
    if value == 1:
        currency = amount*0.0113
        symbol = 'USD'
    elif value == 2:
        currency = amount*0.00975
        symbol = 'EUR'
    elif value == 3:
        currency = amount*1.7469
        symbol = 'JPY'
    elif value == 4:
        currency = amount*0.0173
        symbol = 'AUD'
    # else:
    #     messagebox.showwarning(Warning, message='Select currency...')
    oplabel.config(text=f'Currency : {currency} {symbol}')


if(__name__ == '__main__'):
    window = Tk()
    window.geometry('300x400')
    window.config(background='Cyan')
    x = IntVar()
    label1 = Label(window, text='Enter Currency in INR : ')
    currency_entry= Entry(window)
    rdo1 = Radiobutton(window, text='USD', bg='Cyan', variable=x, value=1)
    rdo2 = Radiobutton(window, text='EUR', bg='Cyan',variable=x, value=2)
    rdo3 = Radiobutton(window, text='JPY', bg='Cyan',variable=x, value=3)
    rdo4 = Radiobutton(window, text='AUD', bg='Cyan',variable=x, value=4)
    btn = Button(window, text='Change Currency', command=changeCurrency)
    oplabel = Label(window)
    label1.grid(row=1, column= 1)
    currency_entry.grid(row= 1, column=2)
    rdo1.grid(row=2, column=1, columnspan=2)
    rdo2.grid(row=3, column=1, columnspan=2)
    rdo3.grid(row=4, column=1, columnspan=2)
    rdo4.grid(row=5, column=1, columnspan=2)
    btn.grid(row=6, column=1, columnspan=2)
    oplabel.grid(row=7, column=1, columnspan=2)

    window.mainloop()