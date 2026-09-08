# Q8. Use re.compile() to precompile and reuse a username validation pattern.

import re

username_pattern = re.compile(r"^[A-Za-z][A-Za-z0-9_]{4,14}$")

usernames = ["Lucky123", "student_01", "123student", "abc"]

for username in usernames:
    if username_pattern.match(username):
        print(username, "-> Valid")
    else:
        print(username, "-> Invalid")