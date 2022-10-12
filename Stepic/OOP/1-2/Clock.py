class Clock:


    def __init__(self, tm):
        self.__time = tm
        self.set_time(tm)

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm



    def get_time(self):

        return self.__time

    @classmethod
    def __check_time(cls, tm):
        if type(tm) == int and 0 <= tm < 100000:
            return True
        else:
            return False


clock = Clock(4530)
clock.get_time()