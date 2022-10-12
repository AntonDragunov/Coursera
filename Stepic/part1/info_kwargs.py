def info_kwargs(**kwargs):
    k = []
    k = list(kwargs.keys())
    k.sort()
    #print(k)
    for i in k:
        print(i, ': ', kwargs[i], sep='')



info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')