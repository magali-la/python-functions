# functions for math operations
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y


# calculate function - return results using helpers
def calculate(num1, num2, opertion):
    if opertion == "+":
        return add(num1, num2)
    elif opertion == "-":
        return sub(num1, num2)
    elif opertion == "*":
        return mult(num1, num2)
    elif opertion == "/":
        return div(num1, num2)
    else:
        return "Not a valid operator."


# set a dictionary which will hold string operators as keys and an operator method as a value
def do_math():
    try:
        # turn numbers to floats, if it fails it'll quit the script in the expect
        num1 = float(input("Input first number: "))
        num2 = float(input("Input second number: "))
        operation = input("Input operation (+, -, *, /): ")

        # call helper
        result = calculate(num1, num2, operation)

        # this will print the error if its not a valid operator
        print(result)
    
    # this one will return an error if the strings cant be converted to floats
    except ValueError:
        print("Your input is not a number. Try again.")
    
    # this one is for the division by 0, if num2 == 0
    except ZeroDivisionError:
        print("You can't divide by 0. Try again.")


# call it to start the script
do_math()