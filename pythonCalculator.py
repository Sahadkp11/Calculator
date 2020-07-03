from tkinter import *

window=Tk()
window.geometry("250x400+300+300")
window.resizable(0,0)
window.title("Calculator")

Lbl=Label(
    window,text="Label"
    ,anchor= SE,
    font=("verdana",22)
)
Lbl.pack(expand=True,fill="both",)

btnrow1 =Frame(window,bg  ="#000000")
btnrow1.pack(expand=True,fill = "both",)

btnrow2=Frame(window)
btnrow2.pack(expand=True ,fill = "both",)

btnrow3=Frame(window)
btnrow3.pack(expand=True ,fill = "both",)

btnrow4=Frame(window)
btnrow4.pack(expand=True ,fill = "both",)

btn1=Button(btnrow1,
            text="1",
            font=("verdana",22),
            )
btn1.pack(side=LEFT,expand=True,fill="both",)

btn2=Button(btnrow1,
            text="2",
            font=("verdana",22),
            )
btn2.pack(side=LEFT,expand=True,fill="both",)

btn3=Button(btnrow1
            ,text="3",
            font=("verdana",22),
            )
btn3.pack(side=LEFT,expand=True,fill="both",)

btn4=Button(btnrow1,
            text="4",
            font=("verdana",22),
            )
btn4.pack(side=LEFT,expand= True,fill="both",)






btn1=Button(btnrow2,
            text="1",
            font=("verdana",22),
            )
btn1.pack(side=LEFT,expand=True,fill="both",)

btn2=Button(btnrow2,
            text="2",
            font=("verdana",22),
            )
btn2.pack(side=LEFT,expand=True,fill="both",)

btn3=Button(btnrow2,
            text="3",
            font=("verdana",22),
            )
btn3.pack(side=LEFT,expand=True,fill="both",)

btn4=Button(btnrow2,
            text="4",
            font=("verdana",22),
            )
btn4.pack(side=LEFT,expand= True,fill="both",)






btn1=Button(btnrow3,
            text="1",
            font=("verdana",22),
            )
btn1.pack(side=LEFT,expand=True,fill="both",)

btn2=Button(btnrow3,
            text="2",
            font=("verdana",22),
            )
btn2.pack(side=LEFT,expand=True,fill="both",)

btn3=Button(btnrow3
            ,text="3",
            font=("verdana",22),
            )
btn3.pack(side=LEFT,expand=True,fill="both",)

btn4=Button(btnrow3,
            text="4",
            font=("verdana",22),
            )
btn4.pack(side=LEFT,expand= True,fill="both",)








btn1=Button(btnrow4,
            text="1",
            font=("verdana",22),
            )
btn1.pack(side=LEFT,expand=True,fill="both",)

btn2=Button(btnrow4,
            text="2",
            font=("verdana",22),
            )
btn2.pack(side=LEFT,expand=True,fill="both",)

btn3=Button(btnrow4
            ,text="3",
            font=("verdana",22),
            )
btn3.pack(side=LEFT,expand=True,fill="both",)

btn4=Button(btnrow4,
            text="4",
            font=("verdana",22),
            )
btn4.pack(side=LEFT,expand= True,fill="both",)



window.mainloop()


