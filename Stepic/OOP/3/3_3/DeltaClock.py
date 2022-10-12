class DeltaClock:


    def __init__(self, *args):
        self.clock1 = args[0]
        self.clock2 = args[1]

    def different(self):
        if Clock.get_time(self.clock1) - Clock.get_time(self.clock2) < 0:
            return 0
        else:
            return Clock.get_time(self.clock1) - Clock.get_time(self.clock2)

    def set_time(self):
        s = self.different() % 60
        m = (self.different() // 60) % 60
        h = (self.different() // 3600) % 24
        return f"{self.__get_formatted(h)}: {self.__get_formatted(m)}: {self.__get_formatted(s)}"


    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    def __str__(self):
        return f'{self.set_time()}'

    def __len__(self):
        return self.different()

class Clock:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
