# Q2. Use re.search() to find the first match anywhere in a string (extract an email).

import re

text = "My email is student@gmail.com"

pattern = r"[\w.-]+@[\w.-]+\.\w+"

match = re.search(pattern, text)

if match:
    print("Email:", match.group())
else:
    print("Email not found")