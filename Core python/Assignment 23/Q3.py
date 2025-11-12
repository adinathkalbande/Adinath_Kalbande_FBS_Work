# Design a basic calculator to perform +,-,/,*
from tkinter import *
from tkinter import messagebox

def Operation():
    val1 = first_entry.get()
    val2 = second_entry.get()

    choice = x.get()
    if choice== 1:
        operation = int(val1)+int(val2)
    elif choice == 2:
        operation = int(val1)-int(val2)
    elif choice == 3:
        operation = int(val1)*int(val2)
    elif choice == 4:
        operation = int(val1)/int(val2)
    else:
        messagebox.showwarning(Warning, message='Please Select...')
    oplabel.config(text=f'{operation}')
    

if(__name__ == "__main__"):
    window = Tk()
    window.geometry('300x400')
    window.config(background='cyan')
    label1 = Label(window, text='Enter First Number : ')
    first_entry = Entry(window)
    label2 = Label(window, text='Enter Second Number : ')
    second_entry = Entry(window)
    x = IntVar()
    rdo1 = Radiobutton(window, text='Addition', variable=x, value=1)
    rdo2 = Radiobutton(window, text='Substraction', variable=x, value=2)
    rdo3 = Radiobutton(window, text='Multiplication', variable=x, value=3)
    rdo4 = Radiobutton(window, text='Division', variable=x, value=4)
    btn = Button(window, text='Operation', command=Operation)
    oplabel = Label(window)
    label1.grid(row=1, column=1)
    first_entry.grid(row=1, column=2)
    label2.grid(row=2, column=1)
    second_entry.grid(row=2, column=2)
    rdo1.grid(row=3, column=1, columnspan=2)
    rdo2.grid(row=4, column=1, columnspan=2)
    rdo3.grid(row=5, column=1, columnspan=2)
    rdo4.grid(row=6, column=1, columnspan=2)
    btn.grid(row=7, column=1, columnspan=2)
    oplabel.grid(row=8, column=1, columnspan=2)


    window.mainloop()
