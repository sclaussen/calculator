import random
import sys
from tkinter import *


PADX=1
PADY=1
display = ""

def enter(e):
    e.widget.config(highlightbackground="blue", fg="blue")


def leave(e):
    e.widget.config(highlightbackground="white", fg="black")


def label(window, textvariable, row, column, columnspan):
    e = Label(window, textvariable=textvariable, anchor=E, height=2, borderwidth=2, font=('Helvetica', 14), bg="grey", fg="white")
    e.grid(row=row, column=column, columnspan=columnspan, padx=PADX, pady=PADY, sticky=W+E)

def button(window, text, row, column, columnspan, callback):
    button = Button(window, text=text, command=callback, height=2, font=('Helvetica', 14), highlightbackground="white")
    button.grid(row=row, column=column, columnspan=columnspan, padx=PADX, pady=PADY, sticky=W+E)
    button.bind("<Enter>", enter)
    button.bind("<Leave>", leave)


def clearAll():
    print("clearAll")

def modifier(m):
    print("modifier " + str(m))

def number(n):
    global display
    print("Pressed " + str(n))
    value = int(display.get())
    value = value * 10 + n
    display.set(str(value))

def operation(o):
    print("operation " + str(o))

def equals():
    print("equals")

def main():
    global display

    root = Tk()
    root.title("Calculator")
    root.geometry("500x500")

    display = StringVar()

    # e = Entry(root, text="", borderwidth=4, padx=PADX, pady=PADY)
    display.set("0")
    label(root, display, 0, 0, 4)

    button(root, "AC", 1, 0, 1, clearAll)
    button(root, "\u00B1", 1, 1, 1, lambda: modifier("+/-"))
    button(root, "%", 1, 2, 1, lambda: operation("%"))
    button(root, "\u00F7", 1, 3, 1, lambda: operation("/"))

    button(root, "7", 2, 0, 1, lambda: number(7))
    button(root, "8", 2, 1, 1, lambda: number(8))
    button(root, "9", 2, 2, 1, lambda: number(9))
    button(root, "\u00D7", 2, 3, 1, lambda: operation("x"))

    button(root, "4", 3, 0, 1, lambda: number(4))
    button(root, "5", 3, 1, 1, lambda: number(5))
    button(root, "6", 3, 2, 1, lambda: number(6))
    button(root, "-", 3, 3, 1, lambda: operation("-"))

    button(root, "1", 4, 0, 1, lambda: number(1))
    button(root, "2", 4, 1, 1, lambda: number(2))
    button(root, "3", 4, 2, 1, lambda: number(3))
    button(root, "+", 4, 3, 1, lambda: operation("+"))

    button(root, "0", 5, 0, 1, lambda: number(0))
    button(root, ".", 5, 1, 1, lambda: modifier("."))
    button(root, "=", 5, 2, 2, equals)

    button(root, "Exit", 6, 0, 4, root.quit)

    root.mainloop()


main()
