from tkinter import *

window = Tk()

#Entry
num = StringVar()
show = Entry(window, textvariable = num)
show.grid(row = 0, column = 0, columnspan = 5)

#def
def click():
    result = eval(show.get())
    s = str(result)
    show.insert(END, "=" + s)

#def of numbers
def b0():
    show.insert(END, "0")
def b1():
    show.insert(END, 1)
def b2():
    show.insert(END, 2)
def b3():
    show.insert(END, "3")
def b4():
    show.insert(END, "4")
def b5():
    show.insert(END, "5")
def b6():
    show.insert(END, "6")
def b7():
    show.insert(END, "7")
def b8():
    show.insert(END, "8")
def b9():
    show.insert(END, "9")

#def of formula
def plus():
    show.insert(END, "+")
def divide():
    show.insert(END, "/")
def multiply():
    show.insert(END, "*")
def minus():
    show.insert(END, "-")
def point():
    show.insert(END, ".")

#def of equal
def equal():
    click()

#def of clear
def clear():
    show.delete(0,END)
    return

#button
w = 2
b7 = Button(window, text = "7", width = w, command = b7)
b8 = Button(window, text = "8", width = w, command = b8)
b9 = Button(window, text = "9", width = w, command = b9)
b4 = Button(window, text = "4", width = w, command = b4)
b5 = Button(window, text = "5", width = w, command = b5)
b6 = Button(window, text = "6", width = w, command = b6)
b1 = Button(window, text = "1", width = w, command = b1)
b2 = Button(window, text = "2", width = w, command = b2)
b3 = Button(window, text = "3", width = w, command = b3)
b0 = Button(window, text = "0", width = w, command = b0)
b01 = Button(window, text = "/", width = w, command = divide)
b02 = Button(window, text = "C", width = w, command = clear)
b03 = Button(window, text = "*", width = w, command = multiply)
b04 = Button(window, text = "-", width = w, command = minus)
b05 = Button(window, text = ".", width = w, command = point)
b06 = Button(window, text = "=", width = w, command = equal)
b07 = Button(window, text = "+", width = w, command = plus)

#grid
b7.grid(row = 1, column = 0)
b8.grid(row = 1, column = 1)
b9.grid(row = 1, column = 2)
b4.grid(row = 2, column = 0)
b5.grid(row = 2, column = 1)
b6.grid(row = 2, column = 2)
b1.grid(row = 3, column = 0)
b2.grid(row = 3, column = 1)
b3.grid(row = 3, column = 2)
b0.grid(row = 4, column = 0)
b01.grid(row = 1, column = 3)
b02.grid(row = 1, column = 4)
b03.grid(row = 2, column = 3)
b04.grid(row = 3, column = 3)
b05.grid(row = 4, column = 1)
b06.grid(row = 4, column = 2)
b07.grid(row = 4, column = 3)

window.mainloop()