import random
import string

class PasswordService:

    def generate_password(self, length=8, use_digits=True, use_symbols=True):
        chars = string.ascii_letters

        if use_digits:
            chars += string.digits
        if use_symbols:
            chars += string.punctuation

        return ''.join(random.choice(chars) for _ in range(length))
