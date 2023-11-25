from tkinter import *
from tkinter import Tk, Label
from PIL import Image, ImageTk
import calendar

root=Tk()
root.geometry('400x300')
root.title('calendar')


def show():

    m = int(calendar.month.get())
    y = int(calendar.year.get())
    output = calendar.month(y, m)

    cal.insert('end', 1.0)

def clear():
    cal.delete(1.0, "end")


def exit():
    root.destroy()


    img = ImageTk.PhotoImage(Image.open('calendar.png'))
    label = Label(image=img)
    label.place(x = 170, y = 3 )

    m_label = Label(root, text="Month", font=( '10' , 'verdana', 'bold'))
    m_label.place(x=70, y=80)

    month = Spinbox(root, from_=11, to = 12 , width='5')
    month.place(x=140, y=80)

    y_label = Label(root, text="Year", font=('10', 'verdana', 'bold'))
    y_label.place(x=70, y=80)

    year = Spinbox(root, from_=2023, to = 3000 , width='8')
    year.place(x=260, y=80)

    cal = Text(root, width=33, height=8, relief=RIDGE,borderwidth=2)
    cal.place(x= 70, y= 110)

    Show = (Button(root, text='show', font=('verdana', '10', 'bold'), relief=RIDGE, borderwidth=2, command=show))
    Show.place(x= 140 ,y= 250)

    Clear = (Button(root, text='clear', font=('verdana', '10', 'bold'), relief=RIDGE, borderwidth=2, command=show))
    Clear.place(x= 200, y= 250)

    Exit = (Button(root, text='Exit', font=('verdana', '10', 'bold'), relief = RIDGE, borderwidth=2, command=show))
    Exit.place(x= 260, y= 250)
