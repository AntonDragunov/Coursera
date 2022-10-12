class Museum:

    def __init__(self, name):
        self.name = name
        self.exhibits = []


    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        self.exhibits.pop(obj)

    def get_info_exhibit(self, indx):
        return f"Описание экспоната {self.exhibits[indx-1].name}: {self.exhibits[indx-1 ].descr}"




class Picture:
    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr



class Mummies:
    def __init__(self, name, location, descr):
        self.name = name
        self.location = location
        self.descr = descr

class Papyri:
    def __init__(self, name, date, descr):
        self.name = name
        self.date = date
        self.descr = descr


mus = Museum("Эрмитаж")
mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор", "Вдохновляющая, устрашающая, волнующая картина"))
mus.add_exhibit(Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации"))
p = Papyri("Ученья для, не злата ради", "Древняя Россия", "Самое древнее найденное рукописное свидетельство о языках программирования")
mus.add_exhibit(p)
for x in mus.exhibits:
    print(x.descr)