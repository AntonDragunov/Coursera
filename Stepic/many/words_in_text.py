n = list(map(str, input().upper().split()))
words = set()
znaki = ['.', ',', ';', ':', '-', '?', '!']
for item in n:
    a = ''
    for _ in item:
        if _ not in znaki:
            a += _
        else:
            pass
    words.add(a)
print(len(words))
