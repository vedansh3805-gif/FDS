# Q6. Identify Syntax, Runtime and Logical Errors.

# 1. Syntax Error
# Example:
# if 10 > 5
#     print("Correct")
#
# Missing ':' causes SyntaxError.


# 2. Runtime Error
# Example:
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Runtime Error: Division by zero")


# 3. Logical Error
# Program runs but produces the wrong result.

a = 10
b = 5

result = a - b       # Logical error if addition was expected

print("Logical Error Example:", result)