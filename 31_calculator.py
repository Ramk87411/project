# calculator
# add
def add(n1, n2):
    return n1+n2
# subtract
def subtract(n1, n2):
    return n1-n2
# multiply
def multiply(n1, n2):
    return n1*n2
# divide
def divide(n1, n2):
    return n1/n2
operation = {
    "+":  add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = int(input("Enter your first number : "))
    for symbol in operation :
        print(symbol)
    continue_calc = True
    while continue_calc:
        operation_symbol = input("Pick your operation symbol : ")
        num2 = int(input("Enter your second number :"))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f" type y to continue calculating with {answer} or if you want to start a new type n ") =="y":
            num1 = answer 
        else:
            continue_calc = False
            calculator()

calculator()
