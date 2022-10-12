func = lambda x: True if x % 19 == 0 or x % 13 == 0 else False

func = lambda list1: True if list1[0].lower() == 'a' and list1[len(list1)-1].lower() == 'a' else False


print(func('afsdfsdA'))
