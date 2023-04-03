
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
def exponential(x, y):
    if x == 0:
        return 0
    elif y == 0:
        return 1
    elif y > 0:
        result = x
        for i in range(y-1):
            result *= x
        return result
    else:
        return 1 / exponential(x, -y)
    
"""
def btn_ABY():
    global Y
    global A
    global B
    Y = float(Y)
    A = float(A)
    B = float(B)
    result = str(A*(B**Y))
    input.set(result)
    expression=""
"""

# Babylonian Method
def squareRoot(x):
    guess = 0
    result = 1

    while result != guess:
        guess = result
        result = (result + x / result) / 2
    return result

def ln(x):
    prev = 0
    denominator = 1
    y = (x - 1) / (x + 1)
    y2 = y * y
    sum = y
    while sum != prev:
        prev = sum
        denominator += 2
        y *= y2
        sum += y / denominator
    return 2 * sum

def log(x):
    return ln(x) / ln(10)

def logb(x, y):
    numerator =0
    denominator =0

    while x>= y:
        x /= y
        numerator +=1

    for i in range(1,1000):
        if i%2 ==1:
            answer =((x-1) ** i)/i
            denominator += answer
        else:
            answer= ((x-1) ** i)/i
            numerator += answer

    result= numerator -denominator*2
    return result

def btn_gamma():
    global expression
    expression = int(expression)
    result = factorial(expression-1)
    input.set(result)
    expression=""
    
def btn_MAD():
    global values
    median_values = sum(values)/(len(values))
    
    dev=0
    for number in values:
        dev = dev+abs(number - median_values)
    mad = dev/len(values)
    input.set(mad)
    expression=""

def bt_standard():
    global values
    mean = sum(values)/len(values)
    variance = sum(pow(x - mean,2) for x in values)/(len(values)-1)
    std = (variance) **0.5
    input.set(std)
    expression=""
