from . import display

def sin():
    display.input.get()
    display.updateInput('sin')

def btn_arccos():
    global expression
    expression =float(expression)
    result = (3.141592653589793/2) - expression
    sign= 1
    power = expression

    for i in range(1, 1000):
        sign *= -1
        power *= expression * expression
        term = sign * power / (2 * i+1)
        result += term

    input.set(result)
    expression=""

    
def btn_sinh():
    global expression
    expression = float(expression)
    e = 2.718281828459
    result = ((e**expression)-(1/e**expression))/2
    input.set(result)
    expression=""
