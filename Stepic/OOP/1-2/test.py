class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'

p1 = Person()

print(True if (p1.__dict__).keys() else False)
#print(p1.__dict__)