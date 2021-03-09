import tkinter as tk
from tkinter import *
from tkinter import ttk  
from automailer import *
from NEW_RADAR import *

def sel1():
    
    selection = "You selected Python as a course "

    btn1 = Button(root, text = 'Send Mail to Students !', bd = '5',command =send_mail_student  )
    btn1.pack(side = 'top',ipadx =5 , ipady =5 , padx =5 , pady =5)

    btn2 = Button(root, text = 'Send Mail to Faculty !', bd = '5', command =send_data_to_teacher )
    btn2.pack(side = 'top',ipadx =5 , ipady =5 , padx =5 , pady =5)    
    label.config(text = selection)
 
try:
    root = Tk()
    root.geometry('300x300') 
    root.title('Performance Tracker')
    var = IntVar()
    l = Label(root, text = "Choose the Course") 
    l.config(font =("Courier", 12)) 
    l.pack()
    var1 = IntVar()
    var2 = IntVar()
    C1 = Checkbutton(root, text = "Python", variable = var1, \
                    onvalue = 1, offvalue = 0, height=2, \
                    width = 5 , command = sel1)

    C1.pack()

    label = Label(root)
    label.pack()
    root.mainloop()

except IOError:
   print("Cant read file ")

except UnboundLocalError:
    print("Unbound Local Error")  

except SyntaxError:
    print("Syntax error")  

except TypeError:
    print("TypeError")