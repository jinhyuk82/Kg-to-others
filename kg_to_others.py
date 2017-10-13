from tkinter import *

window=Tk()

text_kg=Text(window, height=2, width=5)
text_kg.grid(row=0, column=0)
text_kg.insert(END, "Kg")

e1=Entry(window, width=5)
e1.grid(row=0, column=1)

b1=Button(window, text="Convert")
b1.grid(row=0, column=2)


window.mainloop()
