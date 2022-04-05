from tkinter import *
from tkinter import ttk
window = Tk()

window.geometry("300x200+10+20")
window.title("Welcome to Python Programming")

button = Button(window, text="Button", fg="purple", font=("Impact", 16))
button.place(x=50, y=70)

label = Label(window, text="This is a label", fg="white", bg="black")
label.place(x=100, y=150)

txtfld = Entry(window, text="This is a text field", bd=3)
txtfld.place(x=200, y=150)

v1 = IntVar()
rdbutton = Radiobutton(window, text="Female", variable=v1, value=1)
rdbutton1 = Radiobutton(window, text="Male", variable=v1, value=2)
rdbutton.place(x=170, y=70)
rdbutton1.place(x=170, y=100)

v2 = StringVar()
v2.set('Anemo')
data1 = "Anemo", "Cryo", "Dendro", "Electro", "Geo", "Hydro", "Pyro"
combo = ttk.Combobox(window, values=data1)
combo.place(x=400, y=10)

data = "Pyro", "Cryo", "Hydro", "Geo", "Anemo", "Dendro", "Electro"
lb = Listbox(window, height=7, selectmode="single")
for num in data:
    lb.insert(END, num)
lb.place(x=270, y=10)

window.mainloop()
