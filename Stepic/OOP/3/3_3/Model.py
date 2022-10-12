class Model:

    def __init__(self):
        self.__dicts = {}

    def query(self, **kwargs):
        self.__dicts.update(kwargs)


    def __str__(self):
        if self.__dicts:

            return 'Model: ' + ', '.join([f'{key} = {value}' for key, value in self.__dicts.items()])

        else:
            return 'Model'

model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)0