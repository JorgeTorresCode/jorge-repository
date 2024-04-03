from tkinter import *

window = Tk()
window.title("Calculator")

input = Entry(window, width=20, borderwidth=5, font=("Arial", 16, "bold"))
input.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def buttonadd(number):
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(number))


def calc():
    try:
        result = eval(input.get())
        input.delete(0, END)
        input.insert(0,result)
        
    except:
        input.delete(0, END)
        input.insert(0, "Error")
        

buttons = "7894561230+-/*=.C"

row=1
col=0

font = ('Arial', 12, 'bold')

for i in buttons:
    if i == "=":
        button = Button(window, text=i, width=8, pady=15, font=font, command=calc)
        
    elif i == "C":
        button = Button(window, text=i, width=8, pady=15, font=font, command=lambda: input.delete(0, END))
        
    else:
        button = Button(window, text=i, width=8, pady=15, font=font, command=lambda num=i: buttonadd(num))
        
    button.grid(row=row, column=col)
    col += 1
    
    if col > 2:
        col = 0
        row += 1


window.mainloop()