# Q3. Use re.findall() to extract all positive and negative integers.

import re

text = "The numbers are 25, -10, 45, -30 and 100."

numbers = re.findall(r"[-+]?\d+", text)

print("Numbers:", numbers)