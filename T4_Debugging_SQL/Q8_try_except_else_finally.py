# Q8. Use try-except-else-finally for division.

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    result = a / b

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")

else:
    print("Result =", result)

finally:
    print("Division operation completed.")