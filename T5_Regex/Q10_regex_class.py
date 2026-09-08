# Q10. Create a Regex class for email, password and hex-color validation.

import re

class TextValidator:

    email = re.compile(r"^[\w.-]+@[\w.-]+\.\w+$")
    password = re.compile(r"^(?=.*[A-Z])(?=.*\d).{8,}$")
    hex_color = re.compile(r"^#[0-9A-Fa-f]{6}$")

    def valid_email(self, text):
        return bool(self.email.match(text))

    def valid_password(self, text):
        return bool(self.password.match(text))

    def valid_hex_color(self, text):
        return bool(self.hex_color.match(text))


validator = TextValidator()

print(validator.valid_email("student@gmail.com"))
print(validator.valid_password("Password123"))
print(validator.valid_hex_color("#FF5733"))