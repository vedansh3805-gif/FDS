# Q9. Use lookahead and lookbehind to extract prices after $ and keys before :.

import re

text = "Price $500 $1200 and key:value"

prices = re.findall(r"(?<=\$)\d+", text)

keys = re.findall(r"\b\w+(?=:)", text)

print("Prices:", prices)
print("Keys:", keys)