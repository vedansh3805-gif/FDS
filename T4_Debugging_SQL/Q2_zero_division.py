# Q2. Write a program that handles ZeroDivisionError.

try:
    a = 10
    b = 0

    result = a / b

    print("Result =", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")