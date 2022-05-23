from tkinter import *

window = Tk()
window.title("Final Exam in OOP")
window.geometry("400x300+20+10")

def Find_the_Least():
    L = []
    L.append(eval(ent1.get()))
    L.append(eval(ent2.get()))
    L.append(eval(ent3.get()))
    entleast.set(min(L))

lbl1=Label(window, text="Find the Least Number", font="bold")
lbl1.place(x=115,y=30)

lbl2=Label(window, text="Enter the first number:")
lbl2.place(x=30,y=75)
ent1=StringVar()
txtfld1=Entry(window, bd=3, textvariable=ent1)
txtfld1.place(x=225,y=75)

lbl3=Label(window, text="Enter the second number:")
lbl3.place(x=30,y=110)
ent2=StringVar()
txtfld2=Entry(window, bd=3, textvariable=ent2)
txtfld2.place(x=225,y=110)

lbl4=Label(window, text="Enter the third number:")
lbl4.place(x=30,y=145)
ent3=StringVar()
txtfld3=Entry(window, bd=3, textvariable=ent3)
txtfld3.place(x=225,y=145)

btn1=Button(window, text="Least Number", command=Find_the_Least)
btn1.place(x=140,y=180)
entleast=StringVar()
txtfld4=Entry(window, bd=3, state="readonly", textvariable=entleast)
txtfld4.place(x=115,y=225)

window.mainloop()