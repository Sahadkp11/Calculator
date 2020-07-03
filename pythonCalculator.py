from tkinter import *

window=Tk()
window.geometry("250x400+300+300")
window.resizable(0,0)
window.title("Calculator")


btnrow1 =Frame(window,bg  ="#000000")
btnrow1.pack(expand=True,fill = "both")

btnrow2=Frame(window)
btnrow2.pack(expand=True ,fill = "both")

btnrow3=Frame(window)
btnrow3.pack(expand=True ,fill = "both")

btnrow4=Frame(window)
btnrow4.pack(expand=True ,fill = "both")

btn1=Button(btnrow1,text="1",font=("verdana",22),)
btn1.pack(side=LEFT,expand=True,fill="both")


window.mainloop()


