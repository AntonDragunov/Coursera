with open('nums.txt', 'r', encoding='utf-8') as file:


    result = file.readlines()
print(result)




for item in result:
     zex = ''
     g = item.split()
     print(g)
     print(type(g))
     for j in g:
        print(j)
        if str(j).isdigit():
            zex = zex + j
        else:
            pass
            print(zex)
            #zex = ''
     print(zex)