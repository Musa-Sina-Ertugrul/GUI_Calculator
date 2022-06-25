#!/usr/bin/env python3
from tkinter import *

# initliazing
root = Tk()
root.title("Calculator")
root.geometry("350x600")
root.configure(bg="#3399ff")
root.iconbitmap("Calculator_30001.ico")
equation = StringVar()
equation.set("0")
root_entry = Entry(root, textvariable=equation, justify="right", font=("new times roman", 30))
root_entry.pack(pady=20, padx=20, ipadx=20, ipady=20)
root_frame = Frame(root)
root_frame.pack(padx=20, pady=20)
# function for writing numbers and sings
expression = ""


def press(n):
    global expression
    expression += str(n)
    equation.set(expression)


# function for clear numbers
def clear():
    global expression
    expression = ""
    equation.set("")


# function for calculate
def equal():
    global expression
    total = str(eval(expression))
    expression = total
    equation.set(total)


# buttons
button_1 = Button(root_frame, width=5, height=5, relief="ridge", text="1",
                  bg="#80bfff", font=("new times roman", 12), command=lambda: press(1))
button_1.grid(row=0, column=0)
button_2 = Button(root_frame, width=5, height=5, relief="ridge", text="2", bg="#80bfff",
                  font=("new times roman", 12), command=lambda: press(2))
button_2.grid(row=0, column=1)
button_3 = Button(root_frame, width=5, height=5, relief="ridge", text="3",
                  bg="#80bfff", font=("new times roman", 12), command=lambda: press(3))
button_3.grid(row=0, column=2)
button_4 = Button(root_frame, width=5, height=5, relief="ridge", text="4",
                  bg="#80bfff", font=("new times roman", 12), command=lambda: press(4))
button_4.grid(row=1, column=0)
button_5 = Button(root_frame, width=5, height=5, relief="ridge", text="5",
                  bg="#80bfff", font=("new times roman", 12), command=lambda: press(5))
button_5.grid(row=1, column=1)
button_6 = Button(root_frame, width=5, height=5, relief="ridge", text="6", bg="#80bfff",
                  font=("new times roman", 12), command=lambda: press(6))
button_6.grid(row=1, column=2)
button_7 = Button(root_frame, width=5, height=5, relief="ridge", text="7",
                  bg="#80bfff", font=("new times roman", 12), command=lambda: press(7))
button_7.grid(row=2, column=0)
button_8 = Button(root_frame, width=5, height=5, relief="ridge", text="8", bg="#80bfff",
                  font=("new times roman", 12), command=lambda: press(8))
button_8.grid(row=2, column=1)
button_9 = Button(root_frame, width=5, height=5, relief="ridge", text="9",
                  bg="#80bfff", font=("new times roman", 12), command=lambda: press(9))
button_9.grid(row=2, column=2)
button_x = Button(root_frame, width=5, height=5, relief="ridge", text="*", bg="#80bfff",
                  font=("new times roman", 12), command=lambda: press("*"))
button_x.grid(row=0, column=3)
button_s = Button(root_frame, width=5, height=5, relief="ridge", text="-",
                  bg="#80bfff", font=("new times roman", 12), command=lambda: press("-"))
button_s.grid(row=1, column=3)
button_a = Button(root_frame, width=5, height=5, relief="ridge", text="+", bg="#80bfff",
                  font=("new times roman", 12), command=lambda: press("+"))
button_a.grid(row=2, column=3)
button_d = Button(root_frame, width=5, height=5, relief="ridge", text="/",
                  bg="#80bfff", font=("new times roman", 12), command=lambda: press("/"))
button_d.grid(row=3, column=3)
button_e = Button(root_frame, width=5, height=5, relief="ridge", text="=",
                  bg="#80bfff", font=("new times roman", 12), command=equal)
button_e.grid(row=3, column=0, columnspan=2, sticky="nsew")
button_c = Button(root_frame, width=5, height=5, relief="ridge", text="C",
                  bg="#80bfff", font=("new times roman", 12), command=clear)
button_c.grid(row=3, column=2)
root.mainloop()
