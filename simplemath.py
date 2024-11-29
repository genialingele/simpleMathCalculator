import tkinter as tk

#root
root= tk.Tk()
root.title("Simple Calculator")
root.config(background="#112233")
root.minsize(220,380)

#widgets
##input field or label
welcome = tk.Label(root, text= "Welcome")


##widgets- buttons

#algorithms and logic

##for capturing the button clicked
def numIn(value):
    current = results.get()
    results.delete(0, tk.END)
    results.insert(0, str(current) + str(value))

    welcome.config(text="")
    welcome.config(text=str(current) + str(value))

#operators (add, subtract, multiply, and divide)
def addFn():
    global operator
    operator = "add"
    global num1
    num1 = int(results.get())
    results.delete(0, tk.END)

def subFn():
    global operator
    operator = "sub"
    global num1
    num1 = int(results.get())
    results.delete(0, tk.END)

def multFn():
    global operator
    operator = "mult"
    global num1
    num1 = int(results.get())
    results.delete(0, tk.END)

def divFn():
    global operator
    operator = "div"
    global num1
    num1 = int(results.get())
    results.delete(0, tk.END)

def equalFn():
    num2 = int(results.get())

    #Check the operator
    if operator == "add":
        answer = num1 + num2
        welcome.config(text=answer)

    if operator == "sub":
        answer = num1 - num2
        welcome.config(text=answer)  

    if operator == "mult":
        answer = num1 * num2
        welcome.config(text=answer)

    if operator == "div":
        answer = num1 / num2
        welcome.config(text=answer)

    results.delete(0, tk.END)
    results.insert(0, answer)

def clearFn():
    results.delete(0, tk.END)
    welcome.config(text="Welcome")


def backspace():
    results.delete(0)

###widgets- buttons- numbers
####widgets- buttons- numbers- style of buttons
btnBG = "#334455"
btnFG = "#FFFFFF"
btnBord = 1

button_0 = tk.Button(root, text="0", padx=20, pady=20, bg=btnBG, fg=btnFG, borderwidth= btnBord, command= lambda: numIn(0))
button_1 = tk.Button(root, text="1", padx=20, pady=20, bg=btnBG, fg=btnFG, borderwidth= btnBord,command= lambda: numIn(1))
button_2 = tk.Button(root, text="2", padx=20, pady=20, bg=btnBG, fg=btnFG, borderwidth= btnBord,command= lambda: numIn(2))
button_3 = tk.Button(root, text="3", padx=20, pady=20, bg=btnBG, fg=btnFG, borderwidth= btnBord,command= lambda: numIn(3))
button_4 = tk.Button(root, text="4", padx=20, pady=20, bg=btnBG, fg=btnFG, borderwidth= btnBord,command= lambda: numIn(4))
button_5 = tk.Button(root, text="5", padx=20, pady=20, bg=btnBG, fg=btnFG, borderwidth= btnBord,command= lambda: numIn(5))
button_6 = tk.Button(root, text="6", padx=20, pady=20, bg=btnBG, fg=btnFG, borderwidth= btnBord,command= lambda: numIn(6))
button_7 = tk.Button(root, text="7", padx=20, pady=20, bg=btnBG, fg=btnFG, borderwidth= btnBord,command= lambda: numIn(7))
button_8 = tk.Button(root, text="8", padx=20, pady=20, bg=btnBG, fg=btnFG, borderwidth= btnBord,command= lambda: numIn(8))
button_9 = tk.Button(root, text="9", padx=20, pady=20, bg=btnBG, fg=btnFG, borderwidth= btnBord,command= lambda: numIn(9))
#comma = tk.Button(root, text=",", padx=20, pady=20, bg=btnBG, fg=btnFG, borderwidth= btnBord,command= lambda: numIn(","))


###widgets- buttons- operations
add = tk.Button(root, text="+", padx=20, pady=20, bg=btnBG, fg=btnFG, borderwidth= btnBord,command=addFn)
sub = tk.Button(root, text="-", padx=21, pady=20, bg=btnBG, fg=btnFG, borderwidth= btnBord,command=subFn)
div = tk.Button(root, text="/", padx=21, pady=20, bg=btnBG, fg=btnFG, borderwidth= btnBord,command=divFn)
mult = tk.Button(root, text="x", padx=21, pady=20, bg=btnBG, fg=btnFG, borderwidth= btnBord,command=multFn)

equal = tk.Button(root, text="=", padx=19, pady=20, bg=btnBG, fg=btnFG, borderwidth= btnBord,command=equalFn)
clear = tk.Button(root, text="[x]", padx=16, pady=20, bg=btnBG, fg=btnFG, borderwidth= btnBord,command=clearFn)

#Keyboard listener
root.bind('<Return>',lambda event:equalFn())
root.bind('<Delete>',lambda event:clearFn())
root.bind('<plus>',lambda event:addFn())
root.bind('<minus>',lambda event:subFn())
root.bind('<slash>',lambda event:divFn())
root.bind('<asterisk>',lambda event:multFn())
root.bind('<BackSpace>',lambda event:backspace())


#pack/position

#pack/position - buttons 

#pack/position - buttons - numbers

button_1.grid(column=0, row=5)
button_2.grid(column=1, row=5)
button_3.grid(column=2, row=5)

button_4.grid(column=0, row=4)
button_5.grid(column=1, row=4)
button_6.grid(column=2, row=4)

button_7.grid(column=0, row=3)
button_8.grid(column=1, row=3)
button_9.grid(column=2, row=3)

button_0.grid(column=0, row=6)

#pack/position - buttons - operations
add.grid(column=3, row=6)
sub.grid(column=3, row=5)
mult.grid(column=3, row=4)
div.grid(column=3, row=3)

clear.grid(column=1, row=6)
equal.grid(column=2, row=6)

#pack/position - labels and fields 
welcome = tk.Label(root, text="Welcome", font=("Helvetica", 15), bg="#556677", fg="#FFFFFF", width=20, height=5)
welcome.grid(column=0, row=0, columnspan=4)
results = tk.Entry(root, bg="#CCEEFF", fg="#556677", width=40)
results.grid(column=0, row=1, columnspan=4)

#other

#mainloop
root.mainloop()