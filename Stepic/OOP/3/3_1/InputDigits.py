class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return list(map(int, self.func().split()))


input_dg = InputDigits(input)
res = input_dg()
