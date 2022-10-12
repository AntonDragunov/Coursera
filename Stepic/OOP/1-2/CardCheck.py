from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @classmethod
    def check_card_number(cls, number):
        if len(number) == 19:
            if number[4] == '-' and number[9] == '-' and number[14] == '-':
                for i in range(len(number)):
                    #print(i)
                    if (i + 1) % 5 != 0:
                        if number[i].isdigit():
                            continue
                        else:
                            return False
                            break
                    else:
                        continue
                return True
            else:
                return False

        else:
            return False

    @classmethod
    def check_name(cls, name):
        for i in name:
            print(i)
            if i not in cls.CHARS_FOR_NAME and i != ' ':
                print(False, '1', i)
        if len(name.split()) != 2:
            print(False, '2')
        else:
            return True

    def __init__(self, number, name):
        if self.check_name(name) and self.check_card_number(number):
            self.name = name
            self.number = number


is_number = CardCheck.check_card_number("7770-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")