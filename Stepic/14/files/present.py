with open('class_scores.txt', 'r', encoding='utf-8') as file:
    list1 = file.readlines()

with open('new_scores.txt', 'w+', encoding='utf-8') as file:
    for item in list1:
        s = item.split()

        if int(s[1]) > 95:
            s[1] = 100
        else:
            s[1] = int(s[1]) + 5
        print(*s, file=file, end='\n')
