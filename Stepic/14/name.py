n = str(input())

file = open(n)

languages = file.readlines()
print(*languages)
file.close()