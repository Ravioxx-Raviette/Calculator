import tkinter
from tkinter import *
win = Tk()
def addition():number_result.config(text=f'{int(txtbox1.get())+ int(txtbox2.get())}')
def subtraction():number_result.config(text=f'{int(txtbox1.get())- int(txtbox2.get())}')
def multiply():number_result.config(text=f'{int(txtbox1.get())* int(txtbox2.get())}')
def div():number_result.config(text=f'{int(txtbox1.get())/ int(txtbox2.get())}')
def flrdiv():number_result.config(text=f'{int(txtbox1.get())// int(txtbox2.get())}')
def expo():number_result.config(text=f'{int(txtbox1.get())** int(txtbox2.get())}')
def percent():number_result.config(text=f'{int(txtbox1.get())% int(txtbox2.get())}')
#Title
lblTitle = Label(win, text="Calcu-lator v1", font=("Arial",16), bg="#2D7D9A")
lblTitle.pack()
firsttitle = Label(win, text="First Number", font=("Arial",16),bg="#0099BC")
firsttitle.place (x=10,y=50)
sectitle = Label(win, text="Second Number", font=("Arial",16),bg="#0099BC")
sectitle.place (x=10,y=100)
resulttitle = Label(win, text="Result:", font=("Arial",16),bg="#0099BC")
resulttitle.place (x=10,y=250)
number_result =  Label(win, text="__", font=("Arial",16),bg="#0099BC")
number_result.place (x=100,y=250)
#TXTbox
txtbox1 = Entry(win, width = 25 , font=("Arial", 16))
txtbox1.place(x=170 , y =50)
txtbox2 = Entry(win, width = 25 , font=("Arial", 16))
txtbox2.place(x=170 , y =100)
#button
Addbtn = Button (win, width = 5, text = "+", font = ("Arial", 20), command=addition)
Addbtn.place (x= 5 ,y = 400)
minusbtn = Button (win, width = 5, text = "-", font = ("Arial", 20), command=subtraction )
minusbtn.place (x= 100 ,y = 400)
timesbtn = Button (win, width = 5, text = "x", font = ("Arial", 20), command=multiply )
timesbtn.place (x= 200 ,y = 400)
divbtn = Button (win, width = 5, text = "÷", font = ("Arial", 20), command=div )
divbtn.place (x= 300 ,y = 400)
flrdivbtn = Button (win, width = 5, text = "//", font = ("Arial", 20), command=flrdiv )
flrdivbtn.place (x= 400 ,y = 400)
expbtn = Button (win, width = 5, text = "^", font = ("Arial", 20), command=expo )
expbtn.place (x= 500 ,y = 400)
percentbtn = Button (win, width = 5, text = "%", font = ("Arial", 20), command=percent )
percentbtn.place (x= 600 ,y = 400)
win.title("Calculator")
win. geometry("700x500+610+290")
win.configure(bg="#0099BC")
win.mainloop()