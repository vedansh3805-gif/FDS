# Q7. Use named groups to parse a date into labeled fields using groupdict().

import re

date = "08-09-2026"

pattern = r"(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d{4})"

match = re.search(pattern, date)

if match:
    print(match.groupdict())