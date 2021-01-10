from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=50, bg="light gray", fg="black", borderwidth=3)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + float(second_number))

    if math == "subtraction":
        e.insert(0, f_num - float(second_number))

    if math == "multiplication":
        e.insert(0, f_num * float(second_number))

    if math == "division":
        e.insert(0, f_num / float(second_number))


def button_click(number):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)


deci = "."


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + float(second_number))

    if math == "subtraction":
        e.insert(0, f_num - float(second_number))

    if math == "multiplication":
        e.insert(0, f_num * float(second_number))

    if math == "division":
        e.insert(0, f_num / float(second_number))

    if math == ".":
        e.insert(0, f_num)


def button_subtraction():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def button_multiplication():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)


def button_division():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)


def button_decimal():
    first_number = e.get()
    global f_num
    global math
    math = " "
    f_num = float(first_number)
    e.delete(0, END)


def button_negative():
    first_number = e.get()
    global f_num
    global math
    math = " "
    f_num = float(first_number)
    e.delete(0, END)


button_1 = Button(root, text="1", padx=40, pady=20, bg="light gray", command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, bg="light gray", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=43, pady=20, bg="light gray", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, bg="light gray", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, bg="light gray", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=43, pady=20, bg="light gray", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, bg="light gray", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, bg="light gray", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=43, pady=20, bg="light gray", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, bg="light gray", command=lambda: button_click(0))

button_subtraction = Button(root, text="-", padx=41, pady=20, bg="light gray", command=button_subtraction)
button_multiplication = Button(root, text="×", padx=40, pady=20, bg="light gray", command=button_multiplication)
button_division = Button(root, text="÷", padx=40, pady=20, bg="light gray", command=button_division)
button_add = Button(root, text="+", padx=40, pady=20, bg="light gray", command=button_add)

button_equal = Button(root, text="               =                  ", padx=40, pady=20,
                      bg="light gray", command=button_equal)
button_clear = Button(root, text="          Clear              ", padx=40, pady=20,
                      bg="light gray", command=button_clear)

button_decimal = Button(root, text=".", padx=44, pady=20, bg="light gray", command=lambda: button_click("."))
button_negative = Button(root, text="-", padx=40, pady=20, bg="light gray", command=lambda: button_click("-"))

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=0)
button_clear.grid(row=1, column=0, columnspan=2)
button_equal.grid(row=1, column=2, columnspan=2)

button_subtraction.grid(row=3, column=3)
button_multiplication.grid(row=2, column=3)
button_division.grid(row=5, column=3)
button_add.grid(row=4, column=3)

button_decimal.grid(row=5, column=2)
button_negative.grid(row=5, column=1)

root.mainloop()
