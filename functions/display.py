from tkinter import *

def updateInput(click):
    input.set(input.get() + str(click))

def clearEntry():
    input.set('')

def clearInput():
    previousInput.set('')
    input.set('')

def calculate():
    global input
    previousInput.set(input.get() + str('='))
    input.set(eval(input.get()))

def showFunctions(basicFrame, advFrame, basicButton, advButton, clicked):
    global showBasicFrame, showAdvFrame
    if clicked == 'basic':
        if showBasicFrame:
            basicFrame.place_forget()
            showBasicFrame = False
            basicButton.configure(bg='grey94')
        else:
            advFrame.place_forget()
            basicFrame.place(x=5, y=152)
            showBasicFrame = True
            showAdvFrame = False;
            basicButton.configure(bg='grey70')
            advButton.configure(bg='grey94')
    elif clicked == 'advanced':
        if showAdvFrame:
            advFrame.place_forget()
            showAdvFrame = False
            advButton.configure(bg='grey94')
        else:
            basicFrame.place_forget()
            advFrame.place(x=80, y=152)
            showBasicFrame = False
            showAdvFrame = True
            basicButton.configure(bg='grey94')
            advButton.configure(bg='grey70')

def configureWindow(window):
    global input, previousInput
    input = previousInput = StringVar()
 
    global previousInputField, inputField
    previousResultField = Label(window, width=45, height=1, font='arial 12', bg='lightblue', textvariable=previousInput, anchor=E, justify=RIGHT)
    previousResultField.pack(padx=5)
    inputField = Label(window, width=15, height=1, font=('arial', 32, 'bold'), bg='lightblue', textvariable=input, anchor=E, justify=RIGHT)
    inputField.pack(padx=5)

    buttonFrame = Frame(window, width=400, height=500, bg='grey90')
    buttonFrame.pack(side=BOTTOM)

    global showAdvFrame, showBasicFrame
    basicFrame = Frame(window, width=300, height=120, bg='grey70', relief='raised')
    advFrame = Frame(window, width=300, height=120, bg='grey70', relief='raised')
    showBasicFrame = False
    showAdvFrame = False
    

    sin = Button(basicFrame, text='sin', width=5, height=2, bd=0, bg='grey100', font='arial 12', command=lambda: clearInput()).grid(row=0, column=0, padx=(2,1), pady=(2,1))
    cos = Button(basicFrame, text='cos', width=5, height=2, bd=0, bg='grey100', font='arial 12', command=lambda: clearInput()).grid(row=0, column=1, padx=(1), pady=(2,1))
    tan = Button(basicFrame, text='tan', width=5, height=2, bd=0, bg='grey100', font='arial 12', command=lambda: clearInput()).grid(row=0, column=2, padx=(1,2), pady=(2,1))
    sinh = Button(basicFrame, text='sinh', width=5, height=2, bd=0, bg='grey100', font='arial 12', command=lambda: clearInput()).grid(row=1, column=0, padx=(2,1), pady=(1,2))
    cosh = Button(basicFrame, text='cosh', width=5, height=2, bd=0, bg='grey100', font='arial 12', command=lambda: clearInput()).grid(row=1, column=1, padx=1, pady=(1,2))
    tanh = Button(basicFrame, text='tanh', width=5, height=2, bd=0, bg='grey100', font='arial 12', command=lambda: clearInput()).grid(row=1, column=2, padx=(1,2), pady=(1,2))

    placeholder1 = Button(advFrame, text='sin', width=5, height=2, bd=0, bg='grey100', font='arial 12', command=lambda: clearInput()).grid(row=0, column=0, padx=(2,1), pady=(2,1))
    placeholder2 = Button(advFrame, text='cos', width=5, height=2, bd=0, bg='grey100', font='arial 12', command=lambda: clearInput()).grid(row=0, column=1, padx=(1), pady=(2,1))
    placeholder3 = Button(advFrame, text='tan', width=5, height=2, bd=0, bg='grey100', font='arial 12', command=lambda: clearInput()).grid(row=0, column=2, padx=(1), pady=(1))
    placeholder7 = Button(advFrame, text='tanh', width=5, height=2, bd=0, bg='grey100', font='arial 12', command=lambda: clearInput()).grid(row=0, column=3, padx=(1,2), pady=(1,2))
    placeholder4 = Button(advFrame, text='sinh', width=5, height=2, bd=0, bg='grey100', font='arial 12', command=lambda: clearInput()).grid(row=1, column=0, padx=(2,1), pady=(1,2))
    placeholder5 = Button(advFrame, text='cosh', width=5, height=2, bd=0, bg='grey100', font='arial 12', command=lambda: clearInput()).grid(row=1, column=1, padx=1, pady=(1,2))
    placeholder6 = Button(advFrame, text='tanh', width=5, height=2, bd=0, bg='grey100', font='arial 12', command=lambda: clearInput()).grid(row=1, column=2, padx=(1,2), pady=(1,2))
    placeholder8 = Button(advFrame, text='tanh', width=5, height=2, bd=0, bg='grey100', font='arial 12', command=lambda: clearInput()).grid(row=1, column=2, padx=(1,2), pady=(1,2))
    placeholder9 = Button(advFrame, text='tanh', width=5, height=2, bd=0, bg='grey100', font='arial 12', command=lambda: clearInput()).grid(row=1, column=2, padx=(1,2), pady=(1,2))

    basic = Button(buttonFrame, text='Basic \nFunctions', width=10, height=3, bd=0, bg='grey94', font='arial 12', command=lambda: showFunctions(basicFrame, advFrame, basic, adv, 'basic'))
    basic.grid(row=0, column=0, padx=1, pady=1)
    adv = Button(buttonFrame, text='Advanced \nFunctions', width=10, height=3, bd=0, bg='grey94', font='arial 12', command=lambda: showFunctions(basicFrame, advFrame, basic, adv, 'advanced'))
    adv.grid(row=0, column=1, padx=1, pady=1)
    clear = Button(buttonFrame, text='CE', width=10, height=3, bd=0, bg='grey94', font='arial 12', command=lambda: clearInput()).grid(row=0, column=2, padx=1, pady=1)
    clearEntry = Button(buttonFrame, text='←', width=10, height=3, bd=0, bg='grey94', font='arial 12', command=lambda: clearInput()).grid(row=0, column=3, padx=1, pady=1)
    
    log = Button(buttonFrame, text='log', width=10, height=3, bd=0, bg='grey94', font='arial 12', command=lambda: updateInput('log')).grid(row=1, column=0, padx=1, pady=1)
    sqrt = Button(buttonFrame, text='√', width=10, height=3, bd=0, bg='grey94', font='arial 12', command=lambda: updateInput('sqrt')).grid(row=1, column=1, padx=1, pady=1)
    exponential = Button(buttonFrame, text='𝑛!', width=10, height=3, bd=0, bg='grey94', font='arial 12', command=lambda: updateInput('!')).grid(row=1, column=2, padx=1, pady=1)
    mode = Button(buttonFrame, text='DEG', width=10, height=3, bd=0, bg='grey94', font='arial 12', command=lambda: updateInput('!')).grid(row=1, column=3, padx=1, pady=1)
    #ln = Button(buttonFrame, text='ln', width=10, height=3, bd=0, bg='grey94', font='arial 12', command=lambda: updateInput('ln')).grid(row=1, column=1, padx=1, pady=1)
    
    leftParenthesis = Button(buttonFrame, text ='(', width=10, height=3, bd=0, bg='grey94', font='arial 12', command=lambda: updateInput('(')).grid(row=2, column=0, padx=1, pady=1)
    rightParenthesis = Button(buttonFrame, text =')', width=10, height=3, bd=0, bg='grey94', font='arial 12', command=lambda: updateInput(')')).grid(row=2, column=1, padx=1, pady=1)
    placeholder = Button(buttonFrame, text ='xʸ', width=10, height=3, bd=0, bg='grey94', font='arial 12', command=lambda: updateInput('')).grid(row=2, column=2, padx=1, pady=1)
    divide = Button(buttonFrame, text ='/', width=10, height=3, bd=0, bg='grey94', font='arial 12', command=lambda: updateInput('/')).grid(row=2, column=3, padx=1, pady=1)
    
    num7 = Button(buttonFrame, text='7', width=10, height=3, bd=0, bg='grey100', font='arial 12', command=lambda: updateInput(7)).grid(row=3, column=0, padx=1, pady=1)
    num8 = Button(buttonFrame, text='8', width=10, height=3, bd=0, bg='grey100', font='arial 12', command=lambda: updateInput(8)).grid(row=3, column=1, padx=1, pady=1)
    num9 = Button(buttonFrame, text='9', width=10, height=3, bd=0, bg='grey100', font='arial 12', command=lambda: updateInput(9)).grid(row=3, column=2, padx=1, pady=1)
    multiply = Button(buttonFrame, text='*', width=10, height=3, bd=0, bg='grey94', font='arial 12', command=lambda: updateInput('*')).grid(row=3, column=3, padx=1, pady=1)
    
    num4 = Button(buttonFrame, text='4', width=10, height=3, bd=0, bg='grey100', font='arial 12', command=lambda: updateInput(4)).grid(row=4, column=0, padx=1, pady=1)
    num5 = Button(buttonFrame, text='5', width=10, height=3, bd=0, bg='grey100', font='arial 12', command=lambda: updateInput(5)).grid(row=4, column=1, padx=1, pady=1)
    num6 = Button(buttonFrame, text='6', width=10, height=3, bd=0, bg='grey100', font='arial 12', command=lambda: updateInput(6)).grid(row=4, column=2, padx=1, pady=1)
    minus = Button(buttonFrame, text='-', width=10, height=3, bd=0, bg='grey94', font='arial 12', command=lambda: updateInput('-')).grid(row=4, column=3, padx=1, pady=1)
    
    num1 = Button(buttonFrame, text='1', width=10, height=3, bd=0, bg='grey100', font='arial 12', command=lambda: updateInput(1)).grid(row=5, column=0, padx=1, pady=1)
    num2 = Button(buttonFrame, text='2', width=10, height=3, bd=0, bg='grey100', font='arial 12', command=lambda: updateInput(2)).grid(row=5, column=1, padx=1, pady=1)
    num3 = Button(buttonFrame, text='3', width=10, height=3, bd=0, bg='grey100', font='arial 12', command=lambda: updateInput(3)).grid(row=5, column=2, padx=1, pady=1)
    plus = Button(buttonFrame, text='+', width=10, height=3, bd=0, bg='grey94', font='arial 12', command=lambda: updateInput('+')).grid(row=5, column=3, padx=1, pady=1)
    
    negate = Button(buttonFrame, text='+/-', width=10, height=3, bd=0, bg='grey100', font='arial 12', command=lambda: updateInput('negate')).grid(row=6, column=0, padx=1, pady=1)
    num0 = Button(buttonFrame, text='0', width=10, height=3, bd=0, bg='grey100', font='arial 12', command=lambda: updateInput(0)).grid(row=6, column=1, padx=1, pady=1)
    dot = Button(buttonFrame, text='.', width=10, height=3, bd=0, bg='grey100', font='arial 12', command=lambda: updateInput('.')).grid(row=6, column=2, padx=1, pady=1)
    equal = Button(buttonFrame, text='=', width=10, height=3, bd=0, bg='lightblue', font='arial 12', command=lambda: calculate()).grid(row=6, column=3, padx=1, pady=1)
