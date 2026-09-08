# Q1. Use re.match() to validate that a string starts with a pattern (Indian mobile number).

import re

mobile = "9876543210"

pattern = r"^[6-9]\d{9}$"

if re.match(pattern, mobile):
    print("Valid Indian mobile number")
else:
    print("Invalid Indian mobile number")