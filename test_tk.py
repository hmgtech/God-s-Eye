import sys
import os
import subprocess
from tkinter import *
from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk

def run():
    #os.system('cmd /c "python cmd_command.py"')
    mylabel3 = Label(window,text="Scanned Completed...",font="arial",background="violet").grid(row=6,column=1)
    s2_out = subprocess.check_output([sys.executable, "cmd_command.py"])
    string1 = s2_out.decode("utf-8")
    integer1 = int(string1)
    print("Total people:==>",integer1)
    if integer1>4:
    	label = Label(window, text="Alert!! More people are there: People are:",background="red",font="arial").grid(row=7,column=1,padx="50")
    	label5 = Label(window, text=integer1,background="red",font="arial").grid(row=7,column=2)
    	
def another_tk():
    label = Label(window, text="Information by drone: ",background="yellow",font="arial").grid(row=11,column=1,padx="50")
    s3_out = subprocess.check_output([sys.executable, "gps.py"])

def another2_tk():
    label = Label(window, text="Information by drone: ",background="yellow",font="arial").grid(row=11,column=1,padx="50")
    s3_out = subprocess.check_output([sys.executable, "covid.py"])
    

window = tk.Tk()
window.geometry('425x400')
window.title("God's Eye")
# window.configure(bg='green')
# window.create_line(0,50,400,50,fill='black')
# admin1 = Label(window)
# admin1.grid(row=0,column=0)

# admin11 = Label(window)
# admin11.grid(row=0,column=1)

admin2 = Button(window,text="God's Eye",font="arial")
admin2.grid(row=1,column=1,columnspan=2,padx=150)

admin1111 = Label(window, text="_________________________________________________________________________________")
admin1111.grid(row=2,column=1,columnspan=2)


admin = Button(window,text="Admin Panel",font="arial")
admin.grid(row=3,column=1,columnspan=2,padx=150)

admin111 = Label(window, text="_________________________________________________________________________________")
admin111.grid(row=4,column=1,columnspan=2)

btn = Button(window, text="Test Input", bg="Blue", fg="white",command=run, padx=150,font="arial")
btn.grid(row=5,column=1) 

btn = Button(window, text="COVID19 Qurantined People Details:", bg="Blue", fg="white",command=another_tk, padx=54,font="arial")
btn.grid(row=9,column=1) 

# btn = Button(window, text="COVID19 Qurantined People Details:", bg="Blue", fg="white",command=another2_tk, padx=95,font="arial")
# btn.grid(row=10,column=1) 

window.mainloop()