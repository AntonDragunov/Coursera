class RenderDigit:
    def __call__(self, string, *args, **kwargs):
        try:
            return int(string)
        except:
            return None


class InputValues:

    def __init__(self, render):
        self.__render = render

    def __call__(self, func, *args, **kwargs):  # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            return list(map(self.__render, func(*args, **kwargs).split()))

        return wrapper
render = RenderDigit()
input_dg = InputValues(render)(input)
res = input_dg()
print(res)