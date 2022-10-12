class Recipe:

    def __init__(self, *args):
        self.__spisok = [x for x in args]

    def add_ingredient(self, ing):
        self.__spisok.append(ing)

    def remove_ingredient(self, ing):
        self.__spisok.remove(ing)

    def get_ingredients(self):
        return (self.__spisok)

    def __len__(self):
        return len(self.__spisok)


class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'

#_____________________тесты________________________________-

recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe)  # n = 3

i1 = Ingredient("Соль", 1, "столовая ложка")
i2 = Ingredient("Мука", 1, "кг")
i3 = Ingredient("Мясо баранины", 10, "кг")
i4 = Ingredient("Масло", 100, "гр")

recipe = Recipe(i1, i2, i3)
recipe.add_ingredient(i4)
recipe.remove_ingredient(i3)

assert len(recipe) == 3, "функция len вернула неверное значение"
lst = recipe.get_ingredients()
for x in lst:
    assert isinstance(x, Ingredient), "в списке рецептов должны быть только объекты класса Ingredient"
    assert hasattr(x, 'name') and hasattr(x, 'volume') and hasattr(x,
                                                                   'measure'), "объект класса Ingredient должен иметь атрибуты: name, volume, measure"

assert str(i4) == "Масло: 100, гр", "метод __str__ вернул неверное значение"

i4 = Ingredient("Масло", 120, "гр")
recipe.add_ingredient(i4)
assert len(recipe) == 4, "функция len вернула неверное значение"
