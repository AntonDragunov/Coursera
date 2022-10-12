import time


class GeyserClassic:
    MAX_DATE_FILTER = 100
    SLOT1 = False
    SLOT2 = False
    SLOT3 = False

    def add_filter(self, slot_num, filter):

        if slot_num == 1 and type(filter) == Mechanical and self.SLOT1 == False:
            #print(self.SLOT1,slot_num)
            self.SLOT1 = filter
            #print(self.SLOT1,slot_num)
        elif slot_num == 2 and type(filter) == Aragon and self.SLOT2 == False:
            self.SLOT2 = filter
        elif slot_num == 3 and type(filter) == Calcium and self.SLOT3 == False:
            self.SLOT3 = filter
        else:
            pass
        #print(self.SLOT1, self.SLOT2, self.SLOT3)

    def remove_filter(self, slot_num):
        if slot_num == 1:
            self.SLOT1 = False
        if slot_num == 2:
            self.SLOT2 = False
        if slot_num == 2:
            self.SLOT3 = False

    def get_filters(self):
        return (self.SLOT1, self.SLOT2, self.SLOT3)

    def water_on(self):
        #print(self.SLOT1)
        #print(self.SLOT2)
        #print(self.SLOT3)
        if self.SLOT1 != False and self.SLOT2 != False and self.SLOT3 != False:
            #print('проверка 1')
            res1 = time.time() - self.SLOT1.date
            res2 = time.time() - self.SLOT2.date
            res3 = time.time() - self.SLOT3.date

            if 0.0 <= res1 <= self.MAX_DATE_FILTER and 0.0 <= res2 <= self.MAX_DATE_FILTER and 0.0 <= res3 <= self.MAX_DATE_FILTER:
                return True
            else:
                #print('mistake1')
                return False
        else:
            #print('mistake2')
            return False


class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        else:
            object.__setattr__(self, key, value)


class Aragon:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        else:
            object.__setattr__(self, key, value)


class Calcium:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        else:
            object.__setattr__(self, key, value)


#

my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))

assert my_water.water_on() == False, "метод water_on вернул True, хотя не все фильтры были установлены"

my_water.add_filter(3, Calcium(time.time()))
assert my_water.water_on(), "метод water_on вернул False при всех трех установленных фильтрах"

f1, f2, f3 = my_water.get_filters()
assert isinstance(f1, Mechanical) and isinstance(f2, Aragon) and isinstance(f3, Calcium), "фильтры должны быть устанлены в порядке: Mechanical, Aragon, Calcium"

my_water.remove_filter(1)
assert my_water.water_on() == False, "метод water_on вернул True, хотя один из фильтров был удален"

my_water.add_filter(1, Mechanical(time.time()))
assert my_water.water_on(), "метод water_on вернул False, хотя все три фильтра установлены"

f1, f2, f3 = my_water.get_filters()
my_water.remove_filter(1)

my_water.add_filter(1, Mechanical(time.time() - GeyserClassic.MAX_DATE_FILTER - 1))
assert my_water.water_on() == False, "метод water_on вернул True, хотя у одного фильтра истек срок его работы"

f1 = Mechanical(1.0)
f2 = Aragon(2.0)
f3 = Calcium(3.0)
assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "неверное значение атрибута date в объектах фильтров"

f1.date = 5.0
f2.date = 5.0
f3.date = 5.0

assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "локальный атрибут date в объектах фильтров должен быть защищен от изменения"