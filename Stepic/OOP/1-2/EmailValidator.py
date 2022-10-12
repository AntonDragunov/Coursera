from string import ascii_lowercase, digits, ascii_uppercase
from random import randint



class EmailValidator:
    EMAIL_CHARS = ascii_uppercase + ascii_lowercase + digits + '_.@'
    EMAIL_RANDOM_CHAIRS = ascii_uppercase + ascii_lowercase + digits + '_'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod

    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False

        if not set(email) < set(cls.EMAIL_CHARS):
            return False
        s = email.split('@')
        if len(s) != 2:
            return False
        if len(s[0]) > 100 or len(s[1]) > 50:
            return False

        if "." not in s[1]:
            return False

        if email.count('..') > 0:
            return False
        return True

    @staticmethod
    def __is_email_str(email):
        return type(email) == str

    @classmethod
    def get_random_email(cls):
        n = randint(4, 20)
        length = len(cls.EMAIL_RANDOM_CHAIRS) - 1
        return "".join(cls.EMAIL_RANDOM_CHAIRS[randint(0, length)] for i in range(n)) + "@gmail.com"



