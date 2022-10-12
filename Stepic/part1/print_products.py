def print_products(*args):
    spisok = []
    s = []
    s.append(args)
    #print(s)
    j = 0
    if len(args) != 0:
        for i in args:
            if type(i) is str:
                if i != '':
                    spisok.append(i)
                    #print(spisok)
                else:
                    pass

            else:
                pass
        if len(spisok) != 0:
            for item in spisok:
                j += 1
                print(j, ') ', item, sep='')
        else:
            print('Нет продуктов')





    else:
        return print('Нет продуктов')


# def pechat(spisok)
#     for item in spisok:
#         j += 1
#     return     print(j, ') ', item)


print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
