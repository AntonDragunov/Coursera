a = input()
b = str(a)
i = 0
s = ''
if len(b) > 3:
    c = len(b) // 3
    o = len(b) % 3
    #print(c, o)

    if o == 0:
        #print('количество запятых на 1 меньше!')
        while i < (c-1):
            e = b[-3 - i*3:len(b) - i*3]
            #print('e', e)
            s = ',' + e + s
            i += 1
            #print(i, s)
        s = b[:3] + s
        print(s)
    else:
        #print("количество запятых соответствует!")
        while i < (c):
            e = b[-3 - i*3:len(b) - i*3]
            #print('e', e)
            s = ',' + e + s
            i += 1
            #print(i, s)
        s = b[:len(b)-c*3] + s
        print(s)
else:
    print(b)
