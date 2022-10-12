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
    #result = [(f'{prefix}_{counts}') for counts in range(count)]
    result = [('{}_{}'.format(prefix, counts)) for counts in range(count)]
    return result



print(generate_names('person', 10))


def generate_vampires(count):
    names = generate_names('vampire', count)
    # -> Replace by generator expression
    result = [f'vampire_{counts}' for counts in range(count)]
    return result

#print(generate_vampires(5))

def generate_dragons(count):
    names = generate_names('dragon', count)
    # -> Replace by generator expression
    result = [f'dragon_{counts}' for counts in range(count)]
    return result

def generate_enemies(vampires_count, dragons_count):
    vampires = generate_vampires(vampires_count)
    dragons = generate_dragons(dragons_count)

    enemies = itertools.chain(vampires, dragons)
    from itertools import chain
    vampires = [f'vampires_{vampires_counts}' for vampires_counts in range(vampires_count)]
    dragons = [f'dragons_{dragons_counts}' for dragons_counts in range(dragons_count)]
    total = chain(vampires, dragons)
    return list(total)

print(generate_enemies(40,5))