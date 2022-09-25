from tkinter import *

root = Tk()
root.title('Calculator')
root.resizable(0,0)

entry1 = Entry(root, width=40, borderwidth='5')
entry1.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def click(number):
    current = entry1.get()
    entry1.delete(0, END)
    entry1.insert(0, str(current) + str(number))

def add():
    first_number = entry1.get()
    global f_num
    global math 
    math = 'addition'
    f_num = int(first_number)
    entry1.delete(0, END)

def subtract():
    first_number = entry1.get()
    global f_num
    global math 
    math = 'subtraction'
    f_num = int(first_number)
    entry1.delete(0, END)
def multiply():
    first_number = entry1.get()
    global f_num
    global math 
    math = 'multiplication'
    f_num = int(first_number)
    entry1.delete(0, END)

def divide():
    first_number = entry1.get()
    global f_num
    global math 
    math = 'divison'
    f_num = int(first_number)
    entry1.delete(0, END)

def equal():
    second_number = entry1.get()
    entry1.delete(0, END)
    if math == 'addition':
        entry1.insert(0, f_num + int(second_number))
    elif math == 'subtraction':
        entry1.insert(0, f_num - int(second_number))
    elif math == 'multiplication':
        entry1.insert(0, f_num * int(second_number))
    elif math == 'divison':
        entry1.insert(0, f_num / int(second_number))

def clear():
    entry1.delete(0, END)

button1 = Button(root, text='1', padx=30, pady=20, command=lambda: click(1))
button2 = Button(root, text='2', padx=30, pady=20, command=lambda: click(2))
button3 = Button(root, text='3', padx=30, pady=20, command=lambda: click(3))
button4 = Button(root, text='4', padx=30, pady=20, command=lambda: click(4))
button5 = Button(root, text='5', padx=30, pady=20, command=lambda: click(5))
button6 = Button(root, text='6', padx=30, pady=20, command=lambda: click(6))
button7 = Button(root, text='7', padx=30, pady=20, command=lambda: click(7))
button8 = Button(root, text='8', padx=30, pady=20, command=lambda: click(8))
button9 = Button(root, text='9', padx=30, pady=20, command=lambda: click(9))
button0 = Button(root, text='0', padx=30, pady=20, command=lambda: click(0))
buttonplus = Button(root, text='+', padx=29, pady=20, command= add)
buttonsubtract = Button(root, text='-', padx=31, pady=20, command= subtract)
buttonmultiply = Button(root, text='*', padx=31, pady=20, command= multiply)
buttondivide = Button(root, text='÷', padx=29, pady=20, command= divide)
buttonequal = Button(root, text='=', padx=30, pady=20, command= equal)
buttonclear = Button(root, text='Clear', padx=19, pady=20, command= clear)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)

buttondivide.grid(row=1, column=3)
buttonmultiply.grid(row=2, column=3)
buttonsubtract.grid(row=3, column=3)
buttonplus.grid(row=4, column=3)
buttonequal.grid(row=4, column=2)
buttonclear.grid(row=4, column=1)

root.mainloop()
