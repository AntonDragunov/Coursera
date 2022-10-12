n = str(input())

with open('output.txt', 'w', encoding='utf-8') as file:
    file.writelines(n)
