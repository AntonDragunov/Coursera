# Define a `Robot` class that allows to set `name` (string),
# `arms` (integer, `2` by default) attributes.

# -> Add core here
class Robot:
    def __init__(self, name):
        self.name = name

    arms = 2


# Initialize an instance of the Robot class with name `Wall-E`
# and 2 arms and assign it to a variable `robot1`.

# -> Add core here
robot1 = Robot(name="Wall-E")

# Initialize an instance of the Robot class with name `Grievous`
# and 4 arms and assign it to a variable `robot2`.

# -> Add core here
robot2 = Robot(name="Grievous")
robot2.arms = 4


# Define a `Pizza` class that allows to set `name` (string),
# `ingridients` (list of strings), `size` (integer, by default = 24 (cm)) attributes.

# -> Add core here
class Pizza:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = []

    size = 24


# Initialize an instance of the Pizza class with name `Margherita`,
# ingridients cheese and tomato, and size 32 cm. Assign it to a variable `pizza`.

# -> Add core here
pizza = Pizza(name="Margherita", ingredients=['cheese', 'tomato'])
pizza.size = 32
