# * Complete `generate_names` function by list comprehension:
#   it should return list of names formatted as '{prefix}_{counter}'.
#   Hint: use `range` to iterate over range of integers.
#   Example:
#   >>> generate_names('person', 2)
#   ['person_0', 'person_1']
#
# * Complete 'generate_vampires' and 'generate_dragons' by generators:
#   it should return generator of corresponding instances of classes with
#   appropriate names.
#
# * Complete `generate_enemies` function by dictionary comprehension:
#   it should return dictionary containing enemy name as a key
#   and instance as a value.

import random
import itertools


class Character:
    def __init__(self, name):
        self.name = name


class Enemy(Character):
    pass


class Dragon(Enemy):
    pass


class Vampire(Enemy):
    pass


def generate_names(prefix, count):
    # -> Replace by list comprehension
    # result = [('{prefix}_{counts}') for counts in range(count)]
    result = [('{}_{}'.format(prefix, counts)) for counts in range(count)]
    return result


def generate_vampires(count):
    names = generate_names('vampire', count)
    result = ((Vampire(names)) for names in names)
    return result


def generate_dragons(count):
    names = generate_names('dragon', count)
    result = ((Dragon(names)) for names in names)
    return result


def generate_enemies(vampires_count, dragons_count):
    vampires = generate_vampires(vampires_count)
    dragons = generate_dragons(dragons_count)
    #result = {}
    enemies = itertools.chain(vampires, dragons)
    # -> Replace by dict comprehension
    from itertools import chain
    result = {enemy.name : enemy for enemy in enemies}
    print(result)
    return result
