# Q5. Use re.sub() to mask a card number while keeping the last 4 digits.

import re

card_number = "1234567890123456"

masked = re.sub(r"\d(?=\d{4})", "*", card_number)

print("Original:", card_number)
print("Masked:", masked)