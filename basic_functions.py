def greet_user(name):
    # if empty, then generic message
    if len(name) == 0:
        print("Hello! Welcome!")
    else:
        print(f"Hello, {name}! Welcome!")

# test both
greet_user("Person")
greet_user("")


# add two numberss
def add_two(num1, num2):
    return num1 + num2

result = add_two(2, 4)
print(result)

# check if even using modulo
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
print(f"2 is even: {is_even(2)}")
print(f"5 is even: {is_even(5)}")