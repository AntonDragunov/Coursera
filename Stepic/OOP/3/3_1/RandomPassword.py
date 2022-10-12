import random


class RandomPassword:

    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        passw = ''
        password = [self.psw_chars[random.randint(0, len(self.psw_chars)-1)] for i in range(random.randint(self.min_length, self.max_length))]
        passw += ("".join(password))
            #print(passw)
        #print(type(lst_pass))
        return passw



rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
psw = rnd()
lst_pass = [rnd() for _ in range(3)]
# min_length = 5
# max_length = 20
# psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
