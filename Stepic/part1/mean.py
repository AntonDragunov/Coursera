def mean(*args):

    count = summa = 0
    if int(len(args)) != 0:
        for i in args:
            if type(i) in (int, float):
                count += 1
                summa += i
            # elif int(i):
            #     count += 1
            #     summa += i
            else:
                pass
    else:
        return 0.0
    if summa == 0:
        return 0.0
    else:
        return summa / count


mean()
