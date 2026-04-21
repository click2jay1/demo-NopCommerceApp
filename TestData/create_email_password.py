import string
import random

class Emailpasswordcreator:

    def __init__(self, size):
        self.size = size

    def random_chars_generator(self):
        chars = string.ascii_lowercase + string.digits
        random_word = random.choices(chars, k=self.size)
        return "".join(random_word)

    def create_email(self):
        return self.random_chars_generator() + '@gmail.com'

    def create_password(self):
        return self.random_chars_generator()

