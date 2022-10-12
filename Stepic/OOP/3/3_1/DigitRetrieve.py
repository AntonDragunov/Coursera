class DigitRetrieve:


    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        integer = all(map(lambda x: True if x.isdigit() else False, args[0][1:]))
        #print(integer)
        if integer:

            if (args[0][0]).isdigit or args[0][0] == '-':
                #print(int(args[0]))
                return int(args[0])
            else:
                #print('сработал1')
                return None
        else:
            #print('сработал2', args[0])
            return None





dg = DigitRetrieve()
d1 = dg("123")   # 123 (целое число)
d2 = dg("45.54")   # None (не целое число)
d3 = dg("-56")   # -56 (целое число)
d4 = dg("12fg")  # None (не целое число)
d5 = dg("abc")   # None (не целое число)