# script that divides safely and catches errors

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    finally:
        print("Division operation completed")

# test cases
print(safe_divide(1, 0))
print(safe_divide(1, 2))
print(safe_divide(10, 5))

# unsafe string version 
def unsafe_divide(a, b):
    try:
        return float(a) / float(b)
    except ValueError:
        return "Not a valid pair of numbers"

# will work
print(unsafe_divide(1, "3"))

# won't work
print(unsafe_divide(1, "hello"))
