# Quiz Game: Create an interactive quiz game with multiple-choice questions. Display
# questions one at a time and allow the user to select an answer. Provide feedback on
# whether the selected answer is correct or incorrect.
from tkinter import *
from tkinter import messagebox

def checkAns():
    val = x.get()
    if val == 1:
        answer = 'Wrong Answer'
        oplabel.config(text=f'{answer}', bg='Red')

    elif val == 2:
        answer = 'Correct Answer'
        oplabel.config(text=f'{answer}', bg='Green')
    elif val == 3:
        answer = 'Wrong Answer'
        oplabel.config(text=f'{answer}', bg='Red')

    elif val == 4:
        answer = 'Wrong Answer'
        oplabel.config(text=f'{answer}', bg='Red')

    else:
        messagebox.showwarning(Warning, message="Please Select...")
    # 
if (__name__ == '__main__'):
    Window = Tk()
    Window.geometry('300x400')
    Window.config(bg='Cyan')
    label1 = Label(Window, text='Who establed Maratha Empire?', bg='cyan')
    x = IntVar()
    rdo1 = Radiobutton(Window, text='Maharana Pratap', variable=x, value=1, bg='cyan')
    rdo2 = Radiobutton(Window, text='   Chhatrapati Shivaji Maharaj', variable=x, value=2, bg='cyan')
    rdo3 = Radiobutton(Window, text='Chhatrapati Sambhaji Maharaj', variable=x, value=3, bg='cyan')
    rdo4 = Radiobutton(Window, text='Pruthviraj Chohan', variable=x, value=4, bg='cyan')
    btn = Button(Window, text='Check', command=checkAns)
    oplabel = Label(Window, bg='cyan')

    label1.pack()
    rdo1.pack()
    rdo2.pack()
    rdo3.pack()
    rdo4.pack()
    oplabel.pack()
    btn.pack()
    


    Window.mainloop()


