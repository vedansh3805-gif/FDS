# Q6. Use re.split() to split a string using commas, semicolons and pipes.

import re

text = "Apple,Orange;Banana|Mango;Grapes,Watermelon"

result = re.split(r"[,;|]", text)

print(result)