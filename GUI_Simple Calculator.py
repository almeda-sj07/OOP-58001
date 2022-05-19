from tkinter import *

window = Tk()
window.title("Simple Calculator")
window.geometry("400x300+20+10")

class MyWindow:
    def __init__(self, window):
        self.lbl1 = Label(window, text="Standard Calculator", font=("bold", 12))
        self.lbl1.place(relx=0.50, y=50, anchor='center')

        self.lbl2 = Label(window, text="Input first number:")
        self.lbl2.place(x=50, y=80)
        self.txtfld1 = Entry(window, bd=3)
        self.txtfld1.place(x=200, y=80)

        self.lbl3 = Label(window, text="Input second number:")
        self.lbl3.place(x=50, y=120)
        self.txtfld2 = Entry(window, bd=3)
        self.txtfld2.place(x=200, y=120)

        self.lbl4 = Label(window, text="Choose among the operators")
        self.lbl4.place(x=75, y=160)
        self.btn1 = Button(window, text="Add", command=self.add)
        self.btn1.place(x=75, y=195)
        self.btn2 = Button(window, text="Subtract", command=self.subtract)
        self.btn2.place(x=125, y=195)
        self.btn3 = Button(window, text="Multiply", command=self.multiply)
        self.btn3.place(x=195, y=195)
        self.btn4 = Button(window, text="Divide")
        self.btn4.place(x=265, y=195)
        self.btn4.bind('<Button-1>', self.divide)

        self.lbl5 = Label(window, text="Result:")
        self.lbl5.place(x=100, y=250)
        self.txtfld3 = Entry(window, bd=5)
        self.txtfld3.place(x=160, y=250)

    def add(self):
        self.txtfld3.delete(0, 'end')
        num1 = int(self.txtfld1.get())
        num2 = int(self.txtfld2.get())
        tot = num1+num2
        self.txtfld3.insert(END, str(tot))

    def subtract(self):
        self.txtfld3.delete(0, 'end')
        num1 = int(self.txtfld1.get())
        num2 = int(self.txtfld2.get())
        diff = num1-num2
        self.txtfld3.insert(END, str(diff))

    def multiply(self):
        self.txtfld3.delete(0, 'end')
        num1 = int(self.txtfld1.get())
        num2 = int(self.txtfld2.get())
        prod = num1*num2
        self.txtfld3.insert(END, str(prod))

    def divide(self, event):
        self.txtfld3.delete(0, 'end')
        num1 = int(self.txtfld1.get())
        num2 = int(self.txtfld2.get())
        quot = num1/num2
        self.txtfld3.insert(END, str(quot))

mywin = MyWindow(window)

window.mainloop()
