class Car:
        def __init__(self):
            self.__model = None



        @property
        def model(self):
            return self.__model
        @model.setter
        def model(self, model):
            if type(model) != str:
                pass
            elif 2<= len(model) <= 100:
                self.__model = model
            else:
                pass

