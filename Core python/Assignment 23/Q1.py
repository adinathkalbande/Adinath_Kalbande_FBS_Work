# Develop a simple login system with a username and password field. Implement user
# authentication, and show a success message if the login is successful, or an error
# message if the login fails.
from tkinter import *
from tkinter import messagebox
def login():
    user_value = user_entry.get()
    pass_value = pass_entry.get()
    if user_value == 'admin' and pass_value == '12345':
        messagebox.showinfo(message='Login sucessfully')
    else:
        messagebox.showwarning(Warning, message='Invalid Creadential')
if(__name__ == '__main__'):
    window = Tk()
    window.geometry('300x400')
    window.config(background='Cyan')
    label1 = Label(window, text='Enter Username \t: ', background='Cyan')
    user_entry = Entry(window)
    label2 = Label(window, text='Password \t: ', background='Cyan')
    pass_entry = Entry(window)
    btn = Button(window, text='Login', command=login)
    label1.grid(row=1, column=1)
    user_entry.grid(row=1, column=2)
    label2.grid(row=2, column=1)
    pass_entry.grid(row=2, column=2)
    btn.grid(row=4, column=1, columnspan=2)
    window.mainloop()