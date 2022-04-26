from tkinter import *

window = Tk()
window.geometry("400x300+20+10")
window.title("The Grid Manager")
ent1 = Entry(window, bd=3, justify='center', bg="pink")
ent1.grid(row=0, column=0)
ent1.insert(0, "row 0, column 0")

ent2 = Entry(window, bd=3, justify='center', bg="pink")
ent2.grid(row=0, column=1)
ent2.insert(0, "row 0, column 1")

ent3 = Entry(window, bd=3, justify='center', bg="pink")
ent3.grid(row=0, column=2)
ent3.insert(0, "row 0, column 2")

ent4 = Entry(window, bd=3, justify='center', bg="cyan")
ent4.grid(row=1, column=0)
ent4.insert(0, "row 1, column 0")

ent5 = Entry(window, bd=3, justify='center', bg="cyan")
ent5.grid(row=1, column=1)
ent5.insert(0, "row 1, column 1")

ent6 = Entry(window, bd=3, justify='center', bg="cyan")
ent6.grid(row=1, column=2)
ent6.insert(0, "row 1, column 2")

ent7 = Entry(window, bd=3, justify='center', bg="#AAF0C1")
ent7.grid(row=2, column=0)
ent7.insert(0, "row 2, column 0")

ent8 = Entry(window, bd=3, justify='center', bg="#AAF0C1")
ent8.grid(row=2, column=1)
ent8.insert(0, "row 2, column 1")

ent9 = Entry(window, bd=3, justify='center', bg="#AAF0C1")
ent9.grid(row=2, column=2)
ent9.insert(0, "row 2, column 2")

yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(row=5, column=2, rowspan=4, padx=(0, 100), pady=5)

datalist = "Student1", "Student2", "Student3", "Student4", "Student5", "Student6", "Student7", "Student8", "Student9", "Student10"
var = StringVar()

lb = Listbox(window, listvariable=var, width=10, height=4, bg="#CBC3E3", yscrollcommand=yscroll.set)
lb.grid(row=5, column=1, rowspan=4, padx=(100, 0), pady=5)
var.set(tuple(datalist))
yscroll["command"] = lb.yview()

window.mainloop()
