# Q4. Use re.finditer() to find capitalized words and display their exact positions.

import re

text = "Hello World Python Programming"

pattern = r"\b[A-Z][a-z]*\b"

matches = re.finditer(pattern, text)

for match in matches:
    print("Word:", match.group())
    print("Position:", match.span())