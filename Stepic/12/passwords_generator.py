import random


n = int(input())

m = int(input())


def generate_password(length):
    password = ''
    password = password + str(chr(random.choice(list(range(50, 58)))))
    password = password + str(chr(random.choice(list(range(65, 73)))))
    password = password + str(chr(random.choice(list(range(112, 123)))))
    for z in range(length-3):
        password = password + str(chr(random.choice(new_list)))
    print(password)

def generate_passwords(count, length):
    for i in range(count):
        generate_password(length)




list_simbols = []
new_list = []
#list_simbols.append(list(range(50, 58)))
#list_simbols.append(list(range(65, 73)))
#list_simbols.append(list(range(74, 79)))
list_simbols.append(list(range(80, 91)))
list_simbols.append(list(range(97, 108)))
list_simbols.append(list(range(109, 111)))
list_simbols.append(list(range(112, 123)))

for item in list_simbols:
    for i in item:
        new_list.append(i)

generate_passwords(n, m)


#for item in new_list:
#    print(chr(item))
#print(list_simbols)

#73
#79
#108
#111
#48
#49


#50-57
#65-72, 74-78, 80-95
#97-107, 109-110, 112-122




#
# a = random.randint(65, 90)
# a = random.randint(97, 122)
#
# for i in range(48, 57):
#     print(i, chr(i))


