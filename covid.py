import sys
import os
import subprocess
from tkinter import *
from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk

window = tk.Tk()
window.geometry('520x400')
window.title("Covid19")

admin1111 = Label(window, text="COVID19",font="arial")
admin1111.grid(row=0,column=0)

admin1111 = Label(window, text="__________________________________________________________________________________________________")
admin1111.grid(row=1,column=0,columnspan=2)

admin1111 = Label(window, text="Person ID:1 | GPS | Location: Channi | Time: 12.00PM | Improvement: ✔",font="arial")
admin1111.grid(row=2,column=0)

admin1111 = Label(window, text="_______________________________________________________________________________________________________")
admin1111.grid(row=3,column=0,columnspan=2)

admin1111 = Label(window, text="Person ID:2 | GPS | Location: Alkapuri | Time: 1.00PM | Improvement: ✘",font="arial")
admin1111.grid(row=4,column=0)

admin1111 = Label(window, text="____________________________________________________________________________________________________")
admin1111.grid(row=5,column=0,columnspan=2)

admin1111 = Label(window, text="Person ID:3 | GPS | Location: Alkapuri | Time: 2.00PM | Improvement: ✔ ",font="arial")
admin1111.grid(row=6,column=0)

admin1111 = Label(window, text="___________________________________________________________________________________________________________")
admin1111.grid(row=7,column=0,columnspan=2)

window.mainloop()