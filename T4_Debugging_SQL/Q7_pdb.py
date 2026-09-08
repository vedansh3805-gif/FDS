# Q7. Debug a Python program using pdb
# and identify the statement causing the error.

import pdb


def divide(a, b):
    pdb.set_trace()

    result = a / b

    return result


a = 10
b = 0

print("Result:", divide(a, b))