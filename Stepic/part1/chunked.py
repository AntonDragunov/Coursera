# На вход программе подаются две строки, на одной символы, на другой число nn. Из первой строки формируется список.
# Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает список из чанков указанной длины.
# На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число nn на отдельной строке.
# Программа должна вывести указанный вложенный список.
def chunked(n, list_input):
    new_list = []
    if n < len(list_input):
        i = 0
        j = 1
        while i < len(list_input):
            j = 1
            new_list_2 = []
            if (i + j) == (len(list_input)):
                new_list_2.append(list_input[j - 1 + i])
                new_list.append(new_list_2)
                i = 100
            else:
                while j <= n:
                    new_list_2.append(list_input[j - 1 + i])
                    j += 1

                i += n
                new_list.append(new_list_2)

        return print(new_list)
    else:
        new_list.append(list_input)
        return print(new_list)

# a b c d e f

list_input = list(map(str, input().split()))
n = int(input())
new_list = []
new_list_2 = []
i = 0
j = 0

chunked(n, list_input)
