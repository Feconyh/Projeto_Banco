from tkinter import *
import tkinter as tk


top = Tk()

user_label = Label(top, text="User Name")
user_label.grid(row=0, column=0)

username = Entry(top, bd = 5)
username.grid(row=0, column=1)


def check_vincent():
    if username.get() == "Vincent":
        print ("Hi, Vincent!")
    else:
        print( "Where's Vincent?")

submit_btn = Button(top, text="Submit", width=10, command=check_vincent)
submit_btn.grid(row=3, column=1)

top.mainloop()