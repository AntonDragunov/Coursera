class PhoneBook:

    def __init__(self):
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, indx):
        self.phones.pop(indx)

    def get_phone_list(self):
        return self.phones


class PhoneNumber:

    def __init__(self, number, fio):
        self.number = number
        self.fio = fio
