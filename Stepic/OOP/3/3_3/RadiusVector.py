class RadiusVector:

    def __init__(self, arg1, *args):
        if len(args) == 0:
            self.__coords = [0] * arg1
        else:
            self.__coords = [arg1] + list(args)


    def set_coords(self, *args):
        n = min(len(args), len(self.__coords))

        self.__coords[:n] = args[:n]



    def get_coords(self):
        return (self.__coords)

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return sum(map(lambda x: x ** 2, self.__coords))**0.5

vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11)  # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2)  # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D)  # res_len = 3
res_abs = abs(vector3D)