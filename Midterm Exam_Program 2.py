from tkinter import *
class MyWindow:
    def __init__ (self, win):
        self.lb1 = Label(win, text="Enter your fullname:", fg="red", font=("Calibri", 12))
        self.lb1.place(x=100, y=100)
        self.txtfld1 = Entry(bd=3)
        self.txtfld1.place(x=350, y=100)
        self.button = Button(win, text="Click to display your Fullname", fg="red", font=("Calibri", 12), command=self.click)
        self.button.bind("<Button-1>", self.click)
        self.button.place(x=100, y=150)
        self.txtfld2 = Entry(bd=3)
        self.txtfld2.place(x=350, y=150)
    def click(self):
        fname=str(self.txtfld1.get())
        return self.txtfld2.insert(END, str(fname))

window = Tk()
mywin=MyWindow(window)
window.geometry("600x300")
window.title("Midterm in OOP")

window.mainloop()